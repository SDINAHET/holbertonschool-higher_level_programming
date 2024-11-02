#!/usr/bin/python3
"""
Lists all City objects from the database along with their State names
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Create a connection to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Bind the engine to the Base metadata
    Base.metadata.create_all(engine)

    # Start a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all cities with their associated state names
    results = (session.query(State, City)
                      .filter(State.id == City.state_id)
                      .order_by(City.id)
                      .all())

    # Display the results in the specified format
    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
