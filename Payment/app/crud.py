from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import HTTPException, status

from . import models, schemas

def get_payment(db: Session, payment_id: int):

    return db.query(models.Payment).filter(models.Payment.id == payment_id).first()


def get_payment_by_email(db: Session, email: str):

    return db.query(models.Payment).filter(models.Payment.email == email).first()




def get_payments(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Payment).offset(skip).limit(limit).all()



def create_payment(db: Session, payment: schemas.PaymentCreate):
    print(payment)
    db_payment = models.Payment(amount=payment.amount, ref_id=payment.ref_id, paid_for=models.PayedFor[payment.paid_for], user_id=payment.user_id)
    
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    print(db_payment.paid_for)
    return db_payment
