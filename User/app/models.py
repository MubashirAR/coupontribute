from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .db_connect import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    phone = Column(String(15))
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)