#!/usr/bin/python3
"""
This script interacts with a MySQL database using SQLAlchemy.
It creates a City object associated with a
State object and adds them to the database.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    enname = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(enname)
    Session = sessionmaker(bind=enname)
    session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
