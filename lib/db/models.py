#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, declarative_base

import ipdb

# this is what we edited in line 58, you can name it w.e
engine = create_engine('sqlite:///migrations_dance_match_app.db')

Base = declarative_base()

class Instructor(Base):
    __tablename__ = 'instructors'

    id = Column(Integer(), primary_key = True)
    name = Column(String(), index=True)

    lessons = relationship('Lesson', backref = backref('instructor'))


class Lesson(Base):
    __tablename__ = 'lessons'

    id = Column(Integer(), primary_key = True)
    style = Column(String(), index=True)
    instructor_id = Column(Integer(), ForeignKey('instructors.id'))
    dancer_id = Column(Integer(), ForeignKey('dancers.id'))


class Dancer(Base):
    __tablename__ = 'dancers'

    id = Column(Integer(), primary_key = True)
    name = Column(String(), index=True)

    lessons = relationship('Lesson', backref = backref('dancer'))


# peter = Dancer("Peter")
# joe = Instructor("Joe")
# salsa = Lesson("salsa",joe, peter)

# ipdb.set_trace()