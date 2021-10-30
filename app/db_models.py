import sqlalchemy as _sql
import database as _database


class User(_database.Base):
	__tablename__ = "users"
	user_id = _sql.Column(_sql.Integer, primary_key=True, index=True)
	username = _sql.Column(_sql.String, unique=True, index=True)
	email = _sql.Column(_sql.String, unique=True, index=True)
	full_name = _sql.Column(_sql.String)
	hashed_password = _sql.Column(_sql.String)
	disabled = _sql.Column(_sql.Boolean, default=False)

