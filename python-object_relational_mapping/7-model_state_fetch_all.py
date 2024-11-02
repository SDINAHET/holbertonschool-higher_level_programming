#!/usr/bin/python3
"""
Module 7-model_state_fetch_all.py

Lists all State objects from the database hbtn_0e_6_usa.

This script connects to a MySQL database using SQLAlchemy and retrieves all
State objects, displaying them in ascending order by their id.

Usage:
    ./7-model_state_fetch_all.py <mysql_username> <mysql_password>
    <database_name>

Example:
    ./7-model_state_fetch_all.py root root hbtn_0e_6_usa

Args:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The database name.

Output:
    Displays each state's id and name in the format "<id>: <name>"
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

    # Query all State objects, ordered by id
    states = session.query(State).order_by(State.id).all()

    # Display each state's id and name
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
