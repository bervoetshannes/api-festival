from pydantic import BaseModel, Field

class UserBase(BaseModel):
    class Config:
        orm_mode=True
    email: str

class Location(BaseModel):
    naam: str
    lat: float
    lon: float
    class Config:
        orm_mode=True

class FestivalCreate(BaseModel):
    naam: str
    locatie_id: int
    begin_dat: str
    end_dat: str
    class Config:
        orm_mode=True

class FestivalList(BaseModel):
    naam: str
    locatie: Location
    begin_dat: str
    end_dat: str
    class Config:
        orm_mode=True


class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: str

