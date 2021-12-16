#!/usr/bin/python3
"""
a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where
name matches the argument
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
    cursor.execute("SELECT * FROM states WHERE name LIKE\
    '{:s}' ORDER BY states.id ASC;".format(argv[4]))
    for i in cursor.fetchall():
        if i[1] == argv[4]:
            print(i)

    db.close()
