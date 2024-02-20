from datetime import datetime
from sqlalchemy import desc
from sqlalchemy.orm import Session
from . import models, schemas


def get_last_activity(db: Session):
    last_activity = db.query(models.Activity).order_by(desc(models.Activity.date_created)).first()
    if not last_activity:
        return {}
    return last_activity
