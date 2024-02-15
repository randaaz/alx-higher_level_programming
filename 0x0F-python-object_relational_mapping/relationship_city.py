#!/usr/bin/python3

"""
This module defines the base structure for SQLAlchemy models.
It includes the necessary components for creating mapped classes
representing entities in a MySQL database.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Defines a SQLAlchemy model for a City entity,
    representing a city in a MySQL database.

    Attributes:
    - id (sqlalchemy.Integer): Primary key for the cities table.
    - name (sqlalchemy.String): The name of the city.
    - state_id (sqlalchemy.Integer): Foreign key referencing the id column
                                     in the states table.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
