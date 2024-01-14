#!/usr/bin/python3
"""
This module contain the class defination of a State and an instance Base = declarative_base():
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class:
    - Inherits from Base and represents a table in MySQL called 'states'
    - Column:
        - id (auto-generated, unique integer, can't be null and is a primary key)
        - name (string, maximum 128 characters, can't be null)
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
