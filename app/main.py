from typing import Optional

from datetime import timedelta
from fastapi import Depends, FastAPI, Query, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from classify_message import classify_message
from load_model import load_model

from login_functions import verify_password, get_current_active_user,fake_users_db
from login_schemas import Token, UserBase, UserCreate

import services as _services
from sqlalchemy.orm import Session

ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

_services.create_database()

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(_services.get_db)):
    user = _services.get_user_by_username(db=db, username=form_data.username)
    if not user or not verify_password(form_data.password,user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=UserBase)
def create_user(user: UserCreate, db: Session = Depends(_services.get_db)):
    user_db = _services.get_user_by_username(db=db, username=user.username)
    if user_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    return _services.create_user(db=db, user=user)


@app.get("/users/me")
async def read_users_me(current_user: UserBase = Depends(get_current_active_user)):
	return current_user

@app.get('/')
def get_root(current_user: UserBase = Depends(get_current_active_user)):
	return {'message': 'Welcome to the spam detection API'}

@app.get('/Mlpclassifiers/')
async def Mlpclassifiers(message: Optional[str] = Query(None, max_length=250),current_user: UserBase = Depends(get_current_active_user)):
	sel_model = load_model('MLPClassifier');
	return classify_message(sel_model, message)

@app.get('/Kneighbors/')
async def Kneighbors(message: Optional[str] = Query(None, max_length=250),current_user: UserBase = Depends(get_current_active_user)):
	sel_model = load_model('KNeighbors');
	return classify_message(sel_model, message)

@app.get('/Decisiontrees/')
async def Decisiontrees(message: Optional[str] = Query(None, max_length=250),current_user: UserBase = Depends(get_current_active_user)):
	sel_model = load_model('DecisionTree');
	return classify_message(sel_model, message)

@app.get('/Randomforests/')
async def Randomforests(message: Optional[str] = Query(None, max_length=250),current_user: UserBase = Depends(get_current_active_user)):
	sel_model = load_model('RandomForest');
	return classify_message(sel_model, message)
