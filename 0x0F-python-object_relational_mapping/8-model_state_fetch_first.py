#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)

engine = create_engine(
    'mysql+mysqldb://root:gokuaddicte22@localhost:3306/hbtn_0e_6_usa')
Session = sessionmaker(bind=engine)

session = Session()

for instance in session.query(State).filter_by(id=1):
    print("{}: {}".format(instance.id, instance.name))
session.close()
