#!/usr/bin/python3
"""
Module 9-model_state_filter_a.py

Lists all State objects from the database hbtn_0e_6_usa that contain
the letter 'a' in their name.

Usage:
    ./9-model_state_filter_a.py <mysql_username> <mysql_password>
    <database_name>

Example:
    ./9-model_state_filter_a.py root root hbtn_0e_6_usa

Args:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The database name.

Output:
    Displays each state's id and name that contains the letter 'a',
    sorted by id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Bind engine to Base metadata
    Base.metadata.create_all(engine)

    # Create a new session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for State objects containing the letter 'a'
    states_with_a = (
        session.query(State).filter(State.name.like('%a%'))
        .order_by(State.id).all()
    )

    # Display each state that matches the query
    for state in states_with_a:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
