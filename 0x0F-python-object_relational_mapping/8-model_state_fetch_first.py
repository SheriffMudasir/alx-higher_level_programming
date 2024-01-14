#!/usr/bin/python3
"""
This module prints the first State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def model_state_fetch_first(username, password, db_name):
    """
    This function retrives only the State object from the database hbtn_0e_6_usa and print it
    """

    engine = create_engine(
        'mysql+mysqldb://{}: {}@localhost/{}'.format(username, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_object = session.query(State).order_by(State.id).first()

    if first_object is not None:
        print(f"{first_object.id}: {first_object.name}")
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    model_state_fetch_first(username, password, db_name)
