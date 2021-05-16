import sys
sys.path.append("/app")
try:
    from Payment.app.models import PayedFor
except:
    print('Docker!')
    from app.models import PayedFor
    
from typing import Optional

from sqlalchemy.sql.sqltypes import String
from pydantic import BaseModel

class PaymentBase(BaseModel):
    amount: int
    ref_id: int
    user_id: int

class PaymentCreate(PaymentBase):
    paid_for: str

class Payment(PaymentBase):
    id: int
    paid_for: PayedFor

    class Config:
        orm_mode = True