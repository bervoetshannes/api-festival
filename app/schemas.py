from pydantic import BaseModel, Field

class UserBase(BaseModel):
    class Config:
        orm_mode=True
    email: str

class Location(BaseModel):
    naam: str
    lat: float
    lon: float

class FestivalCreate(BaseModel):
    naam: str
    locatie_id: int

class FestivalList(BaseModel):
    naam: str
    locatie: Location


class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: str

