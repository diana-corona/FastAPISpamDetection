from typing import Optional
from pydantic import BaseModel

class Token(BaseModel):
	access_token: str
	token_type: str

class TokenData(BaseModel):
	username: Optional[str] = None

class User(BaseModel):
	id: int
	username: str
	hashed_password: str
	email: str
	full_name: Optional[str] = None
	disabled: Optional[bool] = None


class UserInDB(User):
	hashed_password: str
