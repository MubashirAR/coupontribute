from typing import List
from datetime import timedelta
import uvicorn
import asyncio, aio_pika
from celery import Celery
from celery.utils.log import get_task_logger
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from kombu import Connection, Exchange
from yosun import Yosun

from . import crud, models, schemas
from .celery import publishers
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
def get_restaurants(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    # publishers.publish()
    return crud.get_restaurants(db, skip=skip, limit=limit)


@app.get("/restaurant/{restaurant_id}", response_model=schemas.Restaurant)
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    db_restaurant = crud.get_restaurant(db, restaurant_id=restaurant_id)
    if db_restaurant is None:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db_restaurant

# async def main(loop):
#     connection = await aio_pika.connect_robust(
#         "amqp://event-bus", loop=loop
#     )

#     queue_name = "hello"

#     async with connection:
#         # Creating channel
#         channel = await connection.channel()
#         print('channel', channel)
#         # Declaring queue
#         queue = await channel.declare_queue(queue_name)

#         async with queue.iterator() as queue_iter:
#             async for message in queue_iter:
#                 async with message.process():
#                     print(message.body)

#                     if queue.name in message.body.decode():
#                         break



# # if __name__ == "__main__":
# #     loop = asyncio.get_event_loop()
# #     loop.run_until_complete(main(loop))
# #     loop.close()

# @app.on_event("startup")
# def startup():
#     loop = asyncio.get_event_loop()
#     asyncio.ensure_future(main(loop))

# import sqlalchemy as sa
# engine = sa.create_engine('mysql://root:example@restaurant-db/')
# insp = sa.inspect(engine)
# db_list = insp.get_schema_names()
# print('db_list')
# print(db_list)
# db = SessionLocal()
# rests = db.query('information_schema').all()
# print('rests')
# print(rests)
CELERY_DEFAULT_QUEUE = 'hello'
celery_app = Celery('app', broker='pyamqp://event-bus//', backend='db+mysql://root:example@restaurant-db/')
celery_app.control.add_consumer('hello', reply=True, durable= True)
@celery_app.task
def add(x):
    print('test',x)
    return x

