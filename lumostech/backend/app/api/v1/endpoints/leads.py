from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from typing import List
from datetime import datetime
import re

from app.db.session import get_db
from app.models.lead import Lead
from app.schemas.lead import LeadCreate, Lead as LeadSchema
from app.core.telegram import telegram_bot
from app.core.rate_limit import rate_limit

router = APIRouter()

def sanitize_input(text: str) -> str:
    """
    Sanitize input to prevent XSS and SQL injection
    """
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove potentially dangerous characters
    text = re.sub(r'[;\'"\\]', '', text)
    return text.strip()

@router.post("/", response_model=LeadSchema, status_code=status.HTTP_201_CREATED)
@rate_limit(limit=5, period=60)  # 5 requests per minute
async def create_lead(
    request: Request,
    lead: LeadCreate, 
    db: Session = Depends(get_db)
):
    """
    Create a new lead with proper validation and error handling
    """
    try:
        # Sanitize inputs
        sanitized_data = {
            'name': sanitize_input(lead.name),
            'company': sanitize_input(lead.company),
            'email': sanitize_input(lead.email),
            'phone': sanitize_input(lead.phone),
            'service_needed': sanitize_input(lead.service_needed),
            'message': sanitize_input(lead.message),
        }

        # Validate email format
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', sanitized_data['email']):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid email format"
            )

        # Validate phone format
        if not re.match(r'^\+?[\d\s-]{10,}$', sanitized_data['phone']):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid phone format"
            )

        db_lead = Lead(
            **sanitized_data,
            date_submitted=datetime.utcnow()
        )

        try:
            db.add(db_lead)
            db.commit()
            db.refresh(db_lead)
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A lead with this email already exists"
            )
        except SQLAlchemyError as e:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Database error occurred"
            )

        # Send Telegram notification in a separate try block
        try:
            lead_data = {
                **sanitized_data,
                'date_submitted': db_lead.date_submitted.isoformat()
            }
            telegram_bot.send_message(telegram_bot.format_lead_message(lead_data))
        except Exception as e:
            # Log the error but don't fail the request
            print(f"Failed to send Telegram notification: {str(e)}")

        return db_lead

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.get("/leads", response_model=List[LeadSchema])
async def get_leads(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Retrieve a list of leads with pagination.
    """
    leads = db.query(Lead).offset(skip).limit(limit).all()
    return leads 