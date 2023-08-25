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
    location_id = Column(Integer, ForeignKey("location.id"))
    begin_dat = Column(String)
    end_dat = Column(String)
    locatie = relationship("Location", back_populates="festivals")
    
class Location(Base):
    __tablename__ = "location"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    naam = Column(String)
    lat = Column(Double)
    lon = Column(Double)
    festivals = relationship("Festival", back_populates="locatie")

    