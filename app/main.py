from datetime import datetime
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import requests
from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/get_activity/')
def get_activity(activity_request: schemas.ActivityRequest, db: Session = Depends(get_db)):
    last_record = crud.get_last_activity(db)

    response = requests.get(f'https://www.boredapi.com/api/activity?participants={activity_request.participants}')
    response_data = response.json()

    max_attempts = 10
    attempt = 0
    try:
        while (response_data['activity'],) in db.query(models.Activity.activity_name).all():
            if attempt >= max_attempts:
                return {'error': 'all valid activities are already in database'}
            response = requests.get(f'https://www.boredapi.com/api/activity?participants={activity_request.participants}')
            response_data = response.json()
            attempt += 1
    except KeyError:
        return response_data

    new_activity = models.Activity(activity_name=response_data['activity'], activity_type=response_data['type'],
                                   date_created=datetime.now())
    db.add(new_activity)
    db.commit()

    if not last_record:
        return {}

    db.refresh(last_record)

    return last_record
