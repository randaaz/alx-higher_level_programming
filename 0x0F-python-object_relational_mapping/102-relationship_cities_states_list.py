#!/usr/bin/python3
"""
This script retrieves and prints information about cities and their
corresponding states from a MySQL database using SQLAlchemy.
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

    for cy in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(cy.id, cy.name, cy.state.name))
