#!/usr/bin/python3
"""
Module 11-model_state_insert.py

Adds the State object “Louisiana” to the database hbtn_0e_6_usa.

Usage:
    ./11-model_state_insert.py <mysql_username> <mysql_password>
    <database_name>

Args:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The database name.

Output:
    Prints the id of the newly created state.
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

    # Create new State object for "Louisiana" and add it to the session
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the id of the new State object
    print(f"{new_state.id}")

    # Close the session
    session.close()
