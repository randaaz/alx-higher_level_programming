#!/usr/bin/python3
"""
This script connects to a MySQL database using
SQLAlchemy and searches for a specific
state by name in the 'states' table.
If the state is found, it prints the state's ID;
otherwise, it prints "Not found". It utilizes the
'model_state' module, which contains
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

    fd = False
    for st in session.query(State):
        if st.name == sys.argv[4]:
            print("{}".format(st.id))
            fd = True
            break
    if fd is False:
        print("Not found")
