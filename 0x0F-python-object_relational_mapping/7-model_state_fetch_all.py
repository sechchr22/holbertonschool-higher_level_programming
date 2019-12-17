#!/usr/bin/python3

from sys import argv
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)

engine = create_engine(
    'mysql+mysqldb://{}:{}@localhost/{}'
    .format(argv[1], argv[2], argv[3], pool_pre_ping=True))
Session = sessionmaker(bind=engine)

session = Session()

for instance in session.query(State).order_by(State.id):
    print("{}: {}".format(instance.id, instance.name))
