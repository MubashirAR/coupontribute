import enum
from sqlalchemy import Enum, Integer, String, Boolean, ForeignKey, Column
from sqlalchemy.orm import validates

from .db_connect import Base

class PayedFor(enum.Enum):
    coupon = 1


class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    user_id = Column(Integer, nullable=False)
    ref_id = Column(Integer, nullable=False)
    paid_for = Column(Enum(PayedFor), nullable=False)

    # @validates('amount')
    # def min_amount(self, key, amount):
    #     assert amount >= 0
    #     return amount