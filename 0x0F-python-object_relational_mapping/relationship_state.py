#!/usr/bin/python3
"""
This script defines a SQLAlchemy model for a State entity,
representing a state in a MySQL database. It includes a relationship
with the City model, establishing a one-to-many association between
states and cities. The 'cascade' parameter ensures that when a state
is deleted, all associated cities are also deleted.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """Represents a state in a MySQL database.
    __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    cities (sqlalchemy.orm.relationship): One-to-many relationship with cities.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
