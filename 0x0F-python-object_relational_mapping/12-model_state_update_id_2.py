#!/usr/bin/python3

"""
Script changes the name of a State object from the database hbtn_0e_6_usa
"""

from sqlalchemy import (create_engine)
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.commit()