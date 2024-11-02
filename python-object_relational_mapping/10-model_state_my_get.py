#!/usr/bin/python3
"""
Module 10-model_state_my_get.py

Prints the State object with the name passed as an argument from the
database hbtn_0e_6_usa.

Usage:
    ./10-model_state_my_get.py <mysql_username> <mysql_password>
    <database_name> <state_name>

Example:
    ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas

Args:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The database name.
    state_name (str): The name of the state to search.

Output:
    Prints the state id if found; otherwise, "Not found".
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

    # Get the state name to search
    state_name = sys.argv[4]

    # Query for State object with the specified name using parameterized query
    state = session.query(State).filter(State.name == state_name).first()

    # Display result
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()
