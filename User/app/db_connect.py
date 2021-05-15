from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:example@user-db-srv/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    # connect_args={"check_same_thread": False}
)
# create_str = "CREATE DATABASE IF NOT EXISTS postgres;"
# engine.execute(create_str)
# engine.execute("USE postgres;")
# db.create_all()
# db.session.commit()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# Base.metadata.create_all(engine, checkfirst=True)