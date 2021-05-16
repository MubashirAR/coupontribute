from typing import List
from sqlalchemy.orm.session import Session
from fastapi import Depends, FastAPI, HTTPException

from .db_connect import SessionLocal, engine
from . import schemas, crud
app = FastAPI()

def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get('/{payment_id}', response_model=schemas.Payment)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    return crud.get_payment(db)

@app.get('/', response_model=List[schemas.Payment])
def get_payments(db: Session = Depends(get_db)):
    return crud.get_payments(db)

@app.post('/', response_model=schemas.Payment)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    print(payment)
    return crud.create_payment(db, payment)
