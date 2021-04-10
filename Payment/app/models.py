import enum
from sqlalchemy import Enum, Integer, String, Boolean, ForeignKey, Column

from .db_connect import Base

class PayedFor(enum.Enum):
    coupon = 1


class Payment(Base):
    __tablename__ = "payment"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, min = 0)
    user_id = Column(Integer, required=True)
    ref_id = Column(Integer, required=True)
    payed_for = Column(Enum(PayedFor), required=True)