from typing import Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from login_schemas import TokenData, UserInDB, UserBase
import sqlalchemy.orm as orm
from db_functions import get_user_by_username, get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = "035dda8450f218f80ef5dda7ee3093df00e04684b75bb1beb1689bda8d951102"
ALGORITHM = "HS256"


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}


def get_user(db: orm.Session, username: str):
	user =  get_user_by_username(db=db, username= username)
	if user :
		return UserInDB(**user)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
	to_encode = data.copy()
	if expires_delta:
		expire = datetime.utcnow() + expires_delta
	else:
		expire = datetime.utcnow() + timedelta(minutes=15)
	to_encode.update({"exp": expire})
	encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
	return encoded_jwt

async def get_current_user(db: orm.Session = Depends(get_db),token: str = Depends(oauth2_scheme)):
	credentials_exception = HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Could not validate credentials",
		headers={"WWW-Authenticate": "Bearer"},
	)
	credentials_exception1 = HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Could not validate username",
		headers={"WWW-Authenticate": "Bearer"},
	)
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		username: str = payload.get("sub")
		if username is None:
			raise credentials_exception1
		token_data = TokenData(username=username)
	except JWTError:
		raise credentials_exception
	username = get_user_by_username(db=db, username=token_data.username)
	if username is None:
		raise credentials_exception
	return username

async def get_current_active_user(current_user: UserBase = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
