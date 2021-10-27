import database as _database
import sqlalchemy.orm as _orm
import db_models as _db_models

def create_database():
	return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
	db = _database.SessionLocal()
	try:
		yield db
	finally:
		db.close()

def get_user_by_username(db: _orm.Session, username: str):
	return db.query(_db_models.User).filter(_db_models.User.username == username).first()