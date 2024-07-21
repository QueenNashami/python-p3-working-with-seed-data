# app/debug.py

from sqlalchemy.orm import sessionmaker
from models import engine, Game

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Verify the data
print(session.query(Game).count())
print(session.query(Game).first())
