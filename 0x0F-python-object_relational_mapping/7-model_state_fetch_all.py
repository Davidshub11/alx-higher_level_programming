#!/usr/bin/python3
"""
This script lists all State objects
from the database `hbtn_0e_6_usa`.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://user:password@localhost:3306/database', echo = False)
Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()
class State(Base):
    """
    State class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """

for instance in session.query(State).order_by(State.id):
    print('{0}: {1}'.format(instance.id, instance.name))
