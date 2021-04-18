from fastapi import Depends, FastAPI, HTTPException

from .db_connect import SessionLocal, engine
from . import schemas
app = FastAPI()

def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get('/', response_model=schemas.Payment)
def get_payment(payment_id: int, )

@app.get('/', response_model=List[schemas.Payment])
