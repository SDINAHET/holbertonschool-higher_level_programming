#!/usr/bin/python3
"""
Module 8-model_state_fetch_first.py

Prints the first State object from the database hbtn_0e_6_usa.

This script connects to a MySQL database using SQLAlchemy and retrieves the
first State object, displaying it in the format "<id>: <name>". If the table
states is empty, it prints "Nothing".

Usage:
    ./8-model_state_fetch_first.py <mysql_username> <mysql_password>
    <database_name>

Example:
    ./8-model_state_fetch_first.py root root hbtn_0e_6_usa

Args:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The database name.

Output:
    Displays the first state's id and name or "Nothing" if there are no states.
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

    # Query for the first State object
    first_state = session.query(State).order_by(State.id).first()

    # Display the result
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
