#!/usr/bin/python3
"""
This script retrieves data from the
cities and states tables in a MySQL
database using SQLAlchemy and prints
information about each city, including
its ID, name, and the corresponding state's name.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    enname = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=enname)
    session = Session()

    for cy, st in session.query(City, State) \
                         .filter(City.state_id == State.id) \
                         .order_by(City.id):
        print("{}: ({}) {}".format(st.name, cy.id, cy.name))
