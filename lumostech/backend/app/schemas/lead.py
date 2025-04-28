from pydantic import BaseModel, EmailStr
from datetime import datetime

class LeadBase(BaseModel):
    name: str
    company: str
    email: EmailStr
    phone: str
    service_needed: str
    message: str

class LeadCreate(LeadBase):
    pass

class Lead(LeadBase):
    id: int
    date_submitted: datetime

    class Config:
        from_attributes = True 