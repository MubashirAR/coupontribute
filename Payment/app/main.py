from fastapi import Depends, FastAPI, HTTPException

from .db_connect import SessionLocal, engine

app = FastAPI()

def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get('/', response_model=)
