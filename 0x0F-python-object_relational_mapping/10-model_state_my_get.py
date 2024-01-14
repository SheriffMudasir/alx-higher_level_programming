#!/usr/bin/python3
"""
This module prints the State object from the database hbtn_0e_6_usa
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


def model_state_my_get(username, password, db_name, name):
    """
    This function  prints the State object with the name passed as argument
    """

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()

    get_state = session.query(State.id).filter(State.name == name).first()

    if get_state is not None:
        print(get_state[0])
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username, password, db_name, name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    model_state_my_get(username, password, db_name, name)
