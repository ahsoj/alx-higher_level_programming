#!/usr/bin.python3
"""improve the model_state.py"""
#from relationship_city import City
from model_state import Base
import sqlalchemy as sql

class State(Base):
    """
        inherit from Base and \
        attr -> id: int
             -> name: str
        rtype: void
    """
    __tablename__ = 'states'
    __table_args__ = {'extend_existing': True}

    id = sql.Column(
            sql.Integer,
            primary_key=True,
            nullable=False,
            unique=True,
            autoincrement="ignore_fk"
            )
    name = sql.Column(sql.String(128), nullable=False)
    cities = sql.orm.relationship("City", back_populates="states", cascade='all,delete')
