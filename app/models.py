from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from .database import Base


class Activity(Base):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True, index=True)
    activity_name = Column(String, index=True)
    activity_type = Column(String)
    date_created = Column(DateTime, default=datetime.now(), index=True)
