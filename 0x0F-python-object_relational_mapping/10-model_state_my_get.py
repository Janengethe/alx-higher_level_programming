#!/usr/bin/python3
"""
a script that prints the State object with
the name passed as argument from the database
hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    instance = session.query(State).filter_by(name=argv[4]).first()
    if instance:
        print("{:d}".format(instance.id))

    else:
        print("Not found")
    session.close()
