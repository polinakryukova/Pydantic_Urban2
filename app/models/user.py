from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
# import task

class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    secondname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)     # только один элемент может быть уникальным?

    tasks = relationship('Task', back_populates='user')


from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))