#!/usr/bin/python3
""" contains the class definition of a State \
        and an instance Base = declarative_base() """
import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        inherit from Base and \
        attr -> id: int
             -> name: str
        rtype: void
    """
    __tablename__ = 'states'
    id = sql.Column(
            sql.Integer,
            primary_key=True,
            nullable=False,
            unique=True,
            autoincrement="ignore_fk"
            )
    name = sql.Column(sql.String(128), nullable=False)
