from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSON

from patients import db

class Patient(db.Model):
    __tablename__ = 'target'
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    # TODO(tavi) Switch to JSONB after upgrading Postgres to 9.4
    answers = Column(JSON, unique=False)


class Question(db.Model):
    id = Column(Integer, primary_key=True)
    text = Column(Text, unique=False)
    answer = Column(Text, unique=False)
