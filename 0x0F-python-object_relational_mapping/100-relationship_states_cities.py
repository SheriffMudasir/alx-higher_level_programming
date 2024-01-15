#!/usr/bin/python3
"""
This script creates the State “California” with the City “San Francisco” in the database hbtn_0e_100_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys


def create_relationship_objects(username, password, db_name):
    """
    Create the State "California" with the City "San Francisco" in the database hbtn_0e_100_usa
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California", cities=[City(name="San Francisco")])
    session.add(new_state)
    session.commit()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    create_relationship_objects(username, password, db_name)
