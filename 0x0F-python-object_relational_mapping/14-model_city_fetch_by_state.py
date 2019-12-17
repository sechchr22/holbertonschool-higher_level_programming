#!/usr/bin/python3
"""Fetch by state"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import (create_engine)

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.
        format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)

    session = Session()

    instances = session.query(State, City).filter(
        City.state_id == State.id).order_by(City.id).all()

    for ins in instances:
        print("{}: ({}) {}".format(ins.State.name, ins.City.id, ins.City.name))

    session.close()
