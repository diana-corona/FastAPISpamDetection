from typing import Optional

from datetime import timedelta
from fastapi import Depends, FastAPI, Query, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from classify_message import classify_message
from load_model import load_model

from login_functions import verify_password, get_password_hash, get_user, authenticate_user, create_access_token, get_current_user, get_current_active_user, fake_users_db
from login_classes import Token, User

ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

@app.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
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

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
	return current_user

@app.get('/')
def get_root(current_user: User = Depends(get_current_active_user)):
	return {'message': 'Welcome to the spam detection API'}

@app.get('/Mlpclassifiers/')
async def Mlpclassifiers(message: Optional[str] = Query(None, max_length=250),current_user: User = Depends(get_current_active_user)):
	sel_model = load_model('MLPClassifier');
	return classify_message(sel_model, message)

@app.get('/Kneighbors/')
async def Kneighbors(message: Optional[str] = Query(None, max_length=250),current_user: User = Depends(get_current_active_user)):
	sel_model = load_model('KNeighbors');
	return classify_message(sel_model, message)

@app.get('/Decisiontrees/')
async def Decisiontrees(message: Optional[str] = Query(None, max_length=250),current_user: User = Depends(get_current_active_user)):
	sel_model = load_model('DecisionTree');
	return classify_message(sel_model, message)

@app.get('/Randomforests/')
async def Randomforests(message: Optional[str] = Query(None, max_length=250),current_user: User = Depends(get_current_active_user)):
	sel_model = load_model('RandomForest');
	return classify_message(sel_model, message)
