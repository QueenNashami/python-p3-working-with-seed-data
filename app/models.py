# app/models.py

from datetime import datetime
from sqlalchemy import (CheckConstraint, UniqueConstraint,
    Column, DateTime, Integer, String, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

engine = create_engine('sqlite:///migrations_test.db')

Base = declarative_base()

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer(), primary_key=True)
    title = Column(String())
    genre = Column(String())
    platform = Column(String())
    price = Column(Integer())
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    def __repr__(self):
        return f"Game(id={self.id}, title='{self.title}', platform='{self.platform}')"
