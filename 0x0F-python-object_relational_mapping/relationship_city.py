#!/usr/bin/python3
"""
This module contains the class definition of City and an instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class City(Base):
    """
    City class:
        - Inherits from Base and represents a MySQL table called cities.
        - Columns:
            - id (auto-generated, unique integer, can't be null and is a primary key)
            - name (string of 128 characters max and can't be null)
            - state_id (integer, can't be null, foreign key to states.id)
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

