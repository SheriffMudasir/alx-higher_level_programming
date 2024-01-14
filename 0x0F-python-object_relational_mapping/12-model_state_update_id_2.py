#!/usr/bin/python3
"""
This module changes the name of a State object in the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def model_state_update_id(username, password, db_name):
    """
    This function changes the name of the State where id = 2 to "New Mexico"
    """

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_update = session.query(State).filter(State.id == 2).first()

    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    model_state_update_id(username, password, db_name)
