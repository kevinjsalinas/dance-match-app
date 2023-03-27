#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# this is what we edited in line 58, you can name it w.e
engine = create_engine('sqlite:///migrations_dance_match_app.db')

Base = declarative_base()

