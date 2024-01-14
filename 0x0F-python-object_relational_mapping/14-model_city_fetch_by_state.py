#!/usr/bin/python3
"""
This module prints all City objects from the database hbtn_0e_14_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import Base, State
import sys


def model_city_fetch_by_state(username, password, db_name):
    """
    This function retrieves all City objects from the database hbtn_0e_14_usa and prints them
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = session.query(State.name).filter(
            State.id == city.state_id).first()[0]
        print(f"{state_name}: ({city.id}), {city.name}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    model_city_fetch_by_state(username, password, db_name)
