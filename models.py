from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()

class Command(Base):
    __tablename__ = 'commands'

    comand_id = Column(Integer, primary_key=True)
    university = Column(String, nullable=False)
    city = Column(String, nullable=False)
    name = Column(String, nullable=False)

    results = relationship('Result', back_populates='command', cascade="all, delete-orphan")

class Result(Base):
    __tablename__ = 'results'

    play_id = Column(Integer, primary_key=True)
    comand_id = Column(Integer, ForeignKey('comands.comand_id'), nullable=False)
    place = Column(String)
    score = Column(Integer)
    next_level = Column(String)

    game_id = Column(Integer, ForeignKey('games.game_id'), nullable=False)
    comand_id = Column(Integer, ForeignKey('comands.comand_id'), nullable=False)

    command = relationship('Command', back_populates='results')
    game = relationship('Game', back_populates='results')

class Game(Base):
    __tablename__ = 'games'

    game_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    league = Column(String, nullable=False)

    results = relationship('Result', back_populates='game', cascade="all, delete-orphan")


DATABASE_URL = 'postgresql://alisa:2003@localhost:5432/project_database'
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

