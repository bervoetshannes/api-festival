from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import os

import auth
import crud
import models
import schemas
from database import SessionLocal, engine

#external Weather API
import requests

print("ceating tables")
models.Base.metadata.create_all(bind=engine)
print("tables created")

# FastAPI configuratie
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.post("/token/")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, active=False, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    users = crud.get_users(db, skip=skip, limit=limit, active=active)
    print(users)
    return users


@app.get("/festivals/", response_model=list[schemas.FestivalList])
def read_festivals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_festivals = crud.get_festivals(db, skip=skip, limit=limit)
    return db_festivals

@app.get("/locations/", response_model=list[schemas.Location])
def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    locations = crud.get_locations(db, skip=skip, limit=limit)
    return locations

@app.post("/locations/", response_model=schemas.Location)
def create_location(location: schemas.Location, db: Session = Depends(get_db)):
    db_location = crud.create_location(db, location=location)
    return db_location

@app.post("/festivals/", response_model=schemas.FestivalList)
def create_festival(festival: schemas.FestivalCreate, db: Session = Depends(get_db)):
    db_festival = crud.create_festival(db, festival=festival)
    return db_festival

@app.put("/festivals/{festival_id}/", response_model=schemas.FestivalList)
def update_festival(festival_id: str, festival: schemas.FestivalUpdate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_festival = crud.update_festival(db, festival_id=festival_id, festival_update=festival)
    if db_festival is None:
        raise HTTPException(status_code=404, detail="Festival not found")
    return db_festival


@app.delete("/users/{user_id}/", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db=db, user_id=user_id)

