#!/usr/bin/python3
""" contains the class definition of a State \
        and an instance Base = declarative_base() """
import sqlalchemy as sql
from model_state import Base, State


class City(Base):
    """
        inherit from Base and \
        attr -> id: int
             -> name: str
             -> state_id: fk
        rtype: str
    """
    __tablename__ = 'cities'
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
    state_r = sql.orm.relationship("State")

    def __str__(self):
        """ return string value of this class """
        return "{}: ({}) {}".format(self.state_r.name, self.id, self.name)
