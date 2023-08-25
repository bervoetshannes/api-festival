from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

import auth
import models
import schemas


# Festival
def get_festivals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Location).all()


def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Location).all()


def create_location(db: Session, location: schemas.Location):
    db_location = models.Location(lat=location.lat, lon=location.lon, naam=location.naam)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location


def create_festival(db: Session, festival: schemas.FestivalCreate):
    db_festival = models.Festival(naam=festival.naam, location_id=festival.locatie_id, begin_dat=festival.begin_dat,
                                  end_dat=festival.end_dat)
    db.add(db_festival)
    db.commit()
    db.refresh(db_festival)
    return db_festival


# USERS

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100, active: bool = False):
    if active:
        return db.query(models.User).filter(models.User.is_active == 1).offset(skip).limit(limit).all()
    return db.query(models.User).offset(skip).limit(limit).all()


def delete_user(db: Session, user_id: int):
    user = get_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
        return user
    return None
