#!/usr/bin/python3

"""
Module 0-select_states
a script that lists all states
from the database hbtn_0e_0_usa
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
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    for data in cursor.fetchall():
        print(data)
    db.close()
