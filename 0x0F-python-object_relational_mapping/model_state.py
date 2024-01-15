#!/usr/bin/python3
"""
This module contains the class definition of a State and an instance Base = declarative_base():
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

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


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/'.format(sys.argv[1], sys.argv[2]), pool_pre_ping=True)


    engine.execute("CREATE DATABASE IF NOT EXISTS {}".format(sys.argv[3]))


    engine.execute("USE {}".format(sys.argv[3]))


    Base.metadata.create_all(engine)

