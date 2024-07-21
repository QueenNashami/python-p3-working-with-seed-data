# app/seed.py

from sqlalchemy.orm import sessionmaker
from models import engine, Game
from faker import Faker
import random

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

# Add a console message so we can see output when the seed file runs
print("Seeding games...")

# Clear existing data
session.query(Game).delete()
session.commit()

fake = Faker()

# Generate 50 random games
games = [
    Game(
        title=fake.name(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(0, 60)
    )
    for _ in range(50)
]

session.bulk_save_objects(games)
session.commit()

print("Seeding complete.")
