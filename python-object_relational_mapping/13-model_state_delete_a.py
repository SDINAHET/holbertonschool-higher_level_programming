#!/usr/bin/python3
"""
Module 13-model_state_delete_a.py

Deletes all State objects with a name containing the letter 'a'
from the database.

Usage:
    ./13-model_state_delete_a.py <mysql_username> <mysql_password>
    <database_name>

Args:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The database name.
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

    # Query and delete all states with 'a' in their name
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all(
    )
    for state in states_to_delete:
        session.delete(state)
    session.commit()

    # Close the session
    session.close()
