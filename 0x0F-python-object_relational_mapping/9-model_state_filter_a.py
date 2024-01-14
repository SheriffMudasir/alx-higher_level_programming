#!/usr/bin/python3
"""
This module prints the first State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def model_state_filter_a(username, password, db_name):
    """
    This function retrieves all state object and print those that contain a.
    """

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_with_a = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    for state in state_with_a:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    model_state_filter_a(username, password, db_name)
