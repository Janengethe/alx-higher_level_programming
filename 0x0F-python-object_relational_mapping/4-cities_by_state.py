#!/usr/bin/python3
"""
a script that lists all cities from the
database hbtn_0e_4_usa
hbtn_0e_0_usa is to be created by 0-select_states.sql
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name\
    FROM cities ORDER BY cities.id ASC;")
    for i in cursor.fetchall():
        print(i)

    db.close()
