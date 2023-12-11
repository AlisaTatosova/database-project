from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()

class Command(Base):
    __tablename__ = 'commands'

    comand_id = Column(Integer, primary_key=True)
    university = Column(String, nullable=False)
    city = Column(String, nullable=False)
    name = Column(String, nullable=False)

    results = relationship('Result', back_populates='command')

class Result(Base):
    __tablename__ = 'results'

    play_id = Column(Integer, primary_key=True)
    command_id = Column(Integer, ForeignKey('commands.comand_id'), nullable=False)
    place = Column(String)
    score = Column(Integer)
    next_level = Column(String)

    command = relationship('Command', back_populates='results')
    game = relationship('Game', back_populates='results')

class Game(Base):
    __tablename__ = 'games'

    play_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    location = Column(String, nullable=False)
    league = Column(String, nullable=False)

    results = relationship('Result', back_populates='game')

def initialize_database():
    DATABASE_URL = 'postgresql://alisa:2003@localhost:5432/project_database'
    engine = create_engine(DATABASE_URL)

    Base.metadata.create_all(engine)

if __name__ == "__main__":
    initialize_database()
