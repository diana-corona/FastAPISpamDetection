import database 
import sqlalchemy.orm as orm
import db_models
import login_schemas 
from login_functions import get_password_hash

from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_database():
	return database.Base.metadata.create_all(bind=database.engine)
	
def get_db():
	db = database.SessionLocal()
	try:
		yield db
	finally:
		db.close()

def get_user_by_username(db: orm.Session, username: str):
	return db.query(db_models.User).filter(db_models.User.username == username).first()

def create_user(db: orm.Session, user: login_schemas.UserCreate):
	db_user = db_models.User(user_id= user.user_id, username= user.username, 
							  hashed_password= get_password_hash(user.password), 
							  email= user.email, full_name= user.full_name,
							  disabled= user.disabled)
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user
