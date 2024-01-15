#!/usr/bin/python3
"""
This module contains the class definition of State and an instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class:
        - Inherits from Base and represents a MySQL table called states.
        - Columns:
            - id (auto-generated, unique integer, can't be null and is a primary key)
            - name (string of 128 characters max and can't be null)
        - Relationship:
            - cities (represents a relationship with the City class)
                - Cascade delete, meaning if a State object is deleted, all linked City objects will be automatically deleted
                - The reference from a City object to its State should be named 'state'
    """
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
