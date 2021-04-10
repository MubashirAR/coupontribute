from typing import Optional
from pydantic import BaseModel

class PaymentBase(BaseModel):
    amount: int
    ref_id: int
    payed_for: int

class Payment(PaymentBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True