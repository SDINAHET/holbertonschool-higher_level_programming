#!/usr/bin/python3
"""Defines a State class linked to the states table in the MySQL database."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Create a base class for the declarative model
Base = declarative_base()

class State(Base):
    """Represents a state for a MySQL database.

    Attributes:
        id (int): The state's id, primary key, auto-incremented, non-nullable.
        name (str): The state's name, string with max 128 characters,
        non-nullable.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
