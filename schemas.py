# schemas.py

from pydantic import BaseModel
from typing import List

class CommandCreate(BaseModel):
    university: str
    city: str
    name: str

class CommandResponse(CommandCreate):
    comand_id: int

class ResultCreate(BaseModel):
    command_id: int
    place: str
    score: int
    next_level: str

class ResultResponse(ResultCreate):
    play_id: int

class GameCreate(BaseModel):
    name: str
    date: str
    location: str
    league: str

class GameResponse(GameCreate):
    play_id: int

