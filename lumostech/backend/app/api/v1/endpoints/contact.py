from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models.contact import ContactSubmission
from app.schemas.contact import ContactFormCreate, ContactFormResponse

router = APIRouter()

@router.post("/contact", response_model=ContactFormResponse)
async def create_contact_submission(
    contact: ContactFormCreate,
    db: Session = Depends(get_db)
):
    try:
        db_contact = ContactSubmission(
            name=contact.name,
            company_name=contact.company_name,
            email=contact.email,
            phone=contact.phone,
            service=contact.service,
            message=contact.message
        )
        db.add(db_contact)
        db.commit()
        db.refresh(db_contact)
        return db_contact
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="Failed to submit contact form. Please try again later."
        ) 