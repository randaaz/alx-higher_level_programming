#!/usr/bin/python3
"""
This script interacts with a MySQL database using SQLAlchemy.
It retrieves and prints information
about states and their associated cities.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    enname = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=enname)
    session = Session()

    for st in session.query(State).order_by(State.id):
        print("{}: {}".format(st.id, st.name))
        for cy in st.cities:
            print("    {}: {}".format(cy.id, cy.name))
