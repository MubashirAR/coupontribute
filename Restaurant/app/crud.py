from sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi import HTTPException, status

from . import models, schemas, events


def get_restaurant(db: Session, restaurant_id: int):
    print({'restaurant_id': restaurant_id})
    print(db.query(models.Restaurant).first().id)
    return db.query(models.Restaurant).filter(models.Restaurant.id == restaurant_id).first()

def get_restaurants(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Restaurant).offset(skip).limit(limit).all()

def create_restaurant(db: Session, restaurant: schemas.RestaurantCreate):
    db_restaurant = models.Restaurant(name=restaurant.name)
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant
