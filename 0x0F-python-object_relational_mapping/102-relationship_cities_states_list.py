#!/usr/bin/python3
"""
This script updates the name of a state
in a MySQL database using SQLAlchemy.
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

    st = session.query(State).filter_by(id=2).first()
    st.name = "New Mexico"
    session.commit()
