from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List
from models import Command, Result, Game
from schemas import CommandCreate, CommandResponse, ResultCreate, ResultResponse, GameCreate, GameResponse

DATABASE_URL = 'postgresql://alisa:2003@localhost:5432/project_database'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CRUD operations for Command
@app.post("/commands/", response_model=CommandResponse)
def create_command(command: CommandCreate, db: Session = Depends(get_db)):
    db_command = Command(**command.dict())
    db.add(db_command)
    db.commit()
    db.refresh(db_command)
    return db_command

@app.get("/commands/", response_model=List[CommandResponse])
def list_commands(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    commands = db.query(Command).offset(skip).limit(limit).all()
    return commands

@app.get("/commands/{command_id}", response_model=CommandResponse)
def read_command(command_id: int, db: Session = Depends(get_db)):
    command = db.query(Command).filter(Command.comand_id == comand_id).first()
    if command is None:
        raise HTTPException(status_code=404, detail="Command not found")
    return command

@app.delete("/commands/{command_id}", response_model=CommandResponse)
def delete_command(command_id: int, db: Session = Depends(get_db)):
    command = db.query(Command).filter(Command.command_id == command_id).first()
    if command is None:
        raise HTTPException(status_code=404, detail="Command not found")
    db.delete(command)
    db.commit()
    return command

# CRUD operations for Result
@app.post("/results/", response_model=ResultResponse)
def create_result(result: ResultCreate, db: Session = Depends(get_db)):
    db_result = Result(**result.dict())
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result

@app.get("/results/", response_model=List[ResultResponse])
def list_results(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    results = db.query(Result).offset(skip).limit(limit).all()
    return results

@app.get("/results/{result_id}", response_model=ResultResponse)
def read_result(result_id: int, db: Session = Depends(get_db)):
    result = db.query(Result).filter(Result.play_id == result_id).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Result not found")
    return result

@app.delete("/results/{result_id}", response_model=ResultResponse)
def delete_result(result_id: int, db: Session = Depends(get_db)):
    result = db.query(Result).filter(Result.play_id == result_id).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Result not found")
    db.delete(result)
    db.commit()
    return result

# CRUD operations for Game
@app.post("/games/", response_model=GameResponse)
def create_game(game: GameCreate, db: Session = Depends(get_db)):
    db_game = Game(**game.dict())
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game

@app.get("/games/", response_model=List[GameResponse])
def list_games(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    games = db.query(Game).offset(skip).limit(limit).all()
    return games

@app.get("/games/{game_id}", response_model=GameResponse)
def read_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.game_id == game_id).first()
    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

@app.delete("/games/{game_id}", response_model=GameResponse)
def delete_game(game_id: int, db: Session = Depends(get_db)):
    game = db.query(Game).filter(Game.game_id == game_id).first()
    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    db.delete(game)
    db.commit()
    return game

