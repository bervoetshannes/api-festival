from pydantic import BaseModel, Field

class UserBase(BaseModel):
    class Config:
        orm_mode=True
    email: str

class Location(BaseModel):
    lat: float
    lon: float

class Festival(BaseModel):
    naam: str
    locatie: Location

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: str

