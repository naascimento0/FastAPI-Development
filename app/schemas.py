from pydantic import BaseModel, EmailStr
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True # initialized variable

# this is going to automatically inherit all of the fields from PostBase
class PostCreate(PostBase): # PostCreate extends PostBase
    pass

class PostResponse(PostBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
        
    class Config:
        from_attributes = True

