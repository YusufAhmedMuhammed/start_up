from pydantic import BaseModel, EmailStr

class ContactFormBase(BaseModel):
    name: str
    company_name: str
    email: EmailStr
    phone: str
    service: str
    message: str

class ContactFormCreate(ContactFormBase):
    pass

class ContactFormResponse(ContactFormBase):
    id: int

    class Config:
        from_attributes = True 