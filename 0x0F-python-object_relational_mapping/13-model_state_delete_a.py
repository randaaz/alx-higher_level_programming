#!/usr/bin/python3
"""
This script connects to a MySQL database
using SQLAlchemy, queries and retrieves
all State objects with names containing the
letter 'a', and then deletes these
states from the database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    enname = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=enname)
    session = Session()

    sts = session.query(State).filter(State.name.like('%a%')).all()

    for st in sts:
        session.delete(st)

    session.commit()
