#!/usr/bin/python3
"""
Module model_state
contains the class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
__tablename__
