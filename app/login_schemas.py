from typing import Optional
from pydantic import BaseModel

class Token(BaseModel):
	access_token: str
	token_type: str

class TokenData(BaseModel):
	username: Optional[str] = None

class UserBase(BaseModel):
	user_id: int
	username: str
	email: str
	full_name: Optional[str] = None
	disabled: Optional[bool] = False
	class Config:
		orm_mode=True

class UserCreate(UserBase):
	password: str

class UserInDB(UserBase):
	hashed_password: str