from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql://root:example@payment-db/"

engine=create_engine(SQLALCHEMY_DATABASE_URL)

create_str = "CREATE DATABASE IF NOT EXISTS db;"
engine.execute(create_str)
engine.execute('use db;')

SessionLocal = sessionmaker(autocommit=False, autoflush=false, bind=engine)

Base = declarative_base()