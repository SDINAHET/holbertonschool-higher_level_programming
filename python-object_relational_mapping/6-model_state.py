#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State  # Import your Base and State classes

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    # Create an engine and connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
    )

    # Create all tables in the engine
    Base.metadata.create_all(engine)
