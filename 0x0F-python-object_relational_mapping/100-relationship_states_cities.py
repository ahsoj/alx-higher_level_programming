#!/usr/bin/python3
"""create relationship and create row data"""
from relationship_city import City
from relationship_state import State
from sqlalchemy.orm import sessionmaker


def main(engine):
    
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="California")
    session.add(state)
    session.commit()

    city = Citiy(name="San Francisco", state=state)
    session.add(city)
    session.commit()


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]),
            pool_pre_ping=True
            )
    main(engine)

