#!/usr/bin/python3
"""
Model City, module
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """City Class"""

    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False,
                      unique=True, ForeignKey('states.id'))
