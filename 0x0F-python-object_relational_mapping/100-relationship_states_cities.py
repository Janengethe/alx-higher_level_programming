#!/usr/bin/python3
"""
a script that creates the State “California”
with the City “San Francisco” from the database
hbtn_0e_100_usa
"""


from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_s = State(name="California")
    new_c = City(name="San Francisco")
    new_s.cities.append(new_c)

    session.add(new_s)
    session.add(new_c)

    session.commit()
    session.close()
