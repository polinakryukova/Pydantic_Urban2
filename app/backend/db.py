from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///ecommerce.db', echo = True)       # создали движок

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

