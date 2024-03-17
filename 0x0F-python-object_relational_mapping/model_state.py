#!/usr/bin/pyhton3
"""
python file that contains the class definition of
a State and an instance Base = declarative_base()
"""

from sqlalchemy import column, integer, string 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class state(Base):
    """
    State class
    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class
    """

    __tablename__ = 'state'
    id = column(Integer, Primary _key = True)
    name = column(string(100), nullable = False)
