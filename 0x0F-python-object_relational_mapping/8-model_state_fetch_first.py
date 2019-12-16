#!/usr/bin/python3
"""
Prints first state module
"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.
        format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)

    session = Session()

    instance = session.query(State).order_by(State.id).first()
    if not instance:
        print("Nothing")
    else:
        print("{}: {}".format(instance.id, instance.name))
    session.close()
