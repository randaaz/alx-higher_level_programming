#!/usr/bin/python3
"""
This script connects to a MySQL database using SQLAlchemy,
creates a new State object
representing the state of Louisiana,
adds it to the session, commits the changes, and
prints the assigned ID of the new state.
It assumes the 'model_state' module contains
the definition of the 'State' class representing
a state entity in the database.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    enname = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=enname)
    session = Session()

    lo = State(name="Louisiana")
    session.add(lo)
    session.commit()
    print(lo.id)
