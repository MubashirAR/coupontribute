from typing import List
from datetime import timedelta
import uvicorn
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from . import crud, models, schemas
from .db_connect import SessionLocal, engine

# models.Base.metadata.create_all(bind=engine, checkfirst=True)

app = FastAPI()

# Dependency

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()



@app.post("/restaurant/", response_model=schemas.Restaurant)
def create_restaurant(restaurant: schemas.RestaurantCreate, db: Session = Depends(get_db)):
    # db_restaurant = crud.get_restaurant_by_email(db, email=restaurant.email)
    # if db_restaurant:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_restaurant(db=db, restaurant=restaurant)


@app.get("/restaurant/", response_model=List[schemas.Restaurant])
def read_restaurants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_restaurants(db, skip=skip, limit=limit)


@app.get("/restaurant/{restaurant_id}", response_model=schemas.Restaurant)
def read_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = crud.get_restaurant(db, restaurant_id=restaurant_id)
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db_restaurant

