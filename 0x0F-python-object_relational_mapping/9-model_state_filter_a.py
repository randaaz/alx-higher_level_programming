#!/usr/bin/python3
"""
This script connects to a MySQL database using SQLAlchemy
and retrieves information
about states from the 'states' table whose names
contain the letter 'a'. It utilizes
the 'model_state' module, which contains the
definition of the 'State' class
representing a state entity in the database.
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

    for st in session.query(State).order_by(State.id):
        if "a" in st.name:
            print("{}: {}".format(st.id, st.name))
