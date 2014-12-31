from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSON

from patients import db

class Patient(db.Model):
    __tablename__ = 'patient'
    
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    # TODO(tavi) Switch to JSONB after upgrading Postgres to 9.4
    answers = Column(JSON, unique=False)


class Question(db.Model):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    text = Column(Text, unique=False)
    conditional_on = Column(Integer,
                            ForeignKey(
                                'answer.id',
                                use_alter=True,
                                name='fk_conditional_on_answer'),
                            nullable=True)

    def __init__(self, text, conditional_on):
        self.text = text
        self.conditional_on = conditional_on


class Answer(db.Model):
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True)
    text = Column(Text, unique=False)
    question_id = Column(Integer, ForeignKey('question.id'))
