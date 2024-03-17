#!/usr/bin/python3
"""
python file that contains the class definition of
a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    State class
    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """

    __tablename__ = 'state'
    id = column(Integer, Primary_key = True)
    name = column(string(126), nullable = False)
