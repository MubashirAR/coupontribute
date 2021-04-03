from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .db_connect import Base

class Restaurant(Base):
    __tablename__ = "restaurant"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    is_active = Column(Boolean, default=True)