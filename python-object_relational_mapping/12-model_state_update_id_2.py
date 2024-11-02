#!/usr/bin/python3
"""
Module 12-model_state_update_id_2.py

Changes the name of the State where id = 2 to "New Mexico" in the database.

Usage:
    ./12-model_state_update_id_2.py <mysql_username> <mysql_password>
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

    # Query for the state with id = 2 and update its name
    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
