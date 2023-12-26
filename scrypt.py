from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from faker import Faker
from models import Command, Result, Game
from datetime import datetime, timedelta

DATABASE_URL = 'postgresql://alisa:2003@localhost:5432/project_database'

engine = create_engine(DATABASE_URL)
SessionLocal = Session(bind=engine)

fake = Faker()

def create_fake_command():
    return Command(
        university=fake.word(),
        city=fake.city(),
        name=fake.company()
    )

def create_fake_result(command_id):
    return Result(
        command_id=command_id,
        place=fake.word(),
        score=fake.random_int(min=1, max=100),
        next_level=fake.word()
    )

def create_fake_game():
    return Game(
        name=fake.word(),
        date=datetime.now() + timedelta(days=fake.random_int(min=1, max=30)),
        location=fake.city(),
        league=fake.word()
    )

def populate_data(db):
    # Create fake commands
    commands = [create_fake_command() for _ in range(15)]
    db.add_all(commands)
    db.commit()

    # Create fake results
    for command in commands:
        results = [create_fake_result(command.command_id) for _ in range(15)]
        db.add_all(results)
    db.commit()

    # Create fake games
    games = [create_fake_game() for _ in range(10)]
    db.add_all(games)
    db.commit()


