from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from typing import List
from datetime import timedelta

from app.core.database import get_db
from app.core.security import get_current_admin_user, create_access_token
from app.models.lead import Lead
from app.models.user import User
from app.schemas.lead import LeadResponse
from app.schemas.auth import Token, UserCreate

router = APIRouter()

@router.get("/admin/leads", response_model=List[LeadResponse])
async def get_all_leads(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_admin_user),
    db: Session = Depends(get_db)
):
    """
    Retrieve all leads (admin only).
    Requires authentication and admin privileges.
    """
    try:
        leads = db.query(Lead).offset(skip).limit(limit).all()
        return leads
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve leads"
        )

@router.post("/admin/token", response_model=Token)
async def login_for_access_token(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Login endpoint for admin users.
    Returns a JWT token for authentication.
    """
    user = db.query(User).filter(User.email == user_data.email).first()
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough privileges"
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email, "is_admin": user.is_admin},
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"} 