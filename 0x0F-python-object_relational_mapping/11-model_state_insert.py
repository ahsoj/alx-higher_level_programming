#!/usr/bin/python3
"""Create sqlalchemy fetcher selecting item from tables"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def main(engine):
    """
        return item with \
                `fetch_one` method
        rtype: obj
    """
    Session = sessionmaker(bind=engine)
    session = Session()
    user = State(name="Louisiana")
    session.add(user)
    session.commit()
    query = session.new
    print(query)


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine

    engine = create_engine(
            'mysql://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]
                ))
    # Base.metadata.create_all(engine)
    main(engine)
