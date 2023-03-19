#!/usr/bin/python3
"""
improve the model_city.py
"""
#from relationship_state import State
from model_state import Base
import sqlalchemy as sql

class City(Base):
    """
        inherit from Base and \
        attr -> id: int
             -> name: str
             -> state_id: fk
        rtype: str
    """
    __tablename__ = 'cities'
    __table_args__ = {'extend_existing': True}

    id = sql.Column(
            sql.Integer,
            primary_key=True,
            nullable=False,
            unique=True,
            autoincrement="ignore_fk"
            )
    name = sql.Column(sql.String(128), nullable=False)
    state_id = sql.Column(
            sql.Integer, sql.ForeignKey('states.id'), nullable=False)
    states = sql.orm.relationship("State", back_populates="cities", cascade='all,delete')
