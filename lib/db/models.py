#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# this is what we edited in line 58, you can name it w.e
engine = create_engine('sqlite:///migrations_dance_match_app.db')

Base = declarative_base()

class Instructor(Base):
    __tablename__ = 'instructors'

    id = Column(Integer(), primary_key = True)
    name = Column(String(), index=True)

class Lessons(Base):
    __tablename__ = 'instructors'

    id = Column(Integer(), primary_key = True)
    type = Column(String(), index=True)


class Dancers(Base):
    __tablename__ = 'dancers'

    id = Column(Integer(), primary_key = True)
    name = Column(String(), index=True)