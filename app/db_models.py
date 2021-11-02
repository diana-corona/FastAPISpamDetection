import sqlalchemy as sql
import database as db


class User(db.Base):
	__tablename__ = "users"
	user_id = sql.Column(sql.Integer, primary_key=True, index=True)
	username = sql.Column(sql.String, unique=True, index=True)
	email = sql.Column(sql.String, unique=True, index=True)
	full_name = sql.Column(sql.String)
	hashed_password = sql.Column(sql.String)
	disabled = sql.Column(sql.Boolean, default=False)

