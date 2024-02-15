#!/usr/bin/python3
"""
This script defines a SQLAlchemy model for a
City entity, representing a city
in a MySQL database.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents a city in a MySQL database.

    Attributes:
    - __tablename__ (str): The name of the MySQL table to store cities.
    - id (sqlalchemy.Integer): The city's id (primary key).
    - name (sqlalchemy.String): The city's name.
    - state_id (sqlalchemy.Integer): Foreign key referencing the id column in
      the states table.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
