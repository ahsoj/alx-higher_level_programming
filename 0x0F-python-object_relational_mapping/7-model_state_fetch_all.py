#!/usr/bin/python3
"""Create sqlalchemy fetcher selecting item from tables"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def main(engine):
    """
    """
    Session = sessionmaker(bind=engine)
    query = Session().query(State).order_by(State.id.asc()).all()
    for q in query:
        print(q)


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine

    engine = create_engine(
            'mysql://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]
                ))
    # Base.metadata.create_all(engine)
    main(engine)
