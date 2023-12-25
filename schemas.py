from pydantic import BaseModel
from typing import List

class CommandCreate(BaseModel):
    university: str
    city: str
    name: str

class CommandResponse(CommandCreate):
    pass

class ResultCreate(BaseModel):
    comand_id: int
    place: str
    score: int
    next_level: str

class ResultResponse(ResultCreate):
    pass

class GameCreate(BaseModel):
    name: str
    date: str
    location: str
    league: str

class GameResponse(GameCreate):
    pass
