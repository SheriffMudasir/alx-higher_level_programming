#!/usr/bin/python3
"""
This module deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def model_state_delete(username, password, db_name):
    """
    This function deletes all State objects with a name containing the letter 'a'
    """

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    for state in state_to_delete:
        session.delete(state)
    session.commit()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    model_state_delete(username, password, db_name)
