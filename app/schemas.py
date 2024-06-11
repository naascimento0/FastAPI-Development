from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True # initialized variable

# this is going to automatically inherit all of the fields from PostBase
class PostCreate(PostBase): # PostCreate extends PostBase
    pass

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
        
    model_config = ConfigDict(from_attributes=True)

class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse # pydantic model
    
    model_config = ConfigDict(from_attributes=True)

class PostWithVotes(BaseModel):
    Post: PostResponse
    votes: int

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: int = Field(..., le=1)