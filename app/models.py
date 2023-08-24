from database import Base
from sqlalchemy import Column, Boolean, Integer, String, Double, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Festival(Base):
    __tablename__ = "festival"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    naam = Column(String)
    location = relationship("Location")
    
class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    lat = Column(Double)
    lon = Column(Double)
    festival_id = Column(Integer, ForeignKey("festival.id"))

    