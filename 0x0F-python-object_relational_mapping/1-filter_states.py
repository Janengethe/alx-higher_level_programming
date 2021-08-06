#!/usr/bin/python3

import MySQLdb

from sys import argv

db = MySQLdb.connect(host="localhost",
                     port=3306,
                     user=argv[1],
                     password=argv[2],
                     database=argv[3]
)
cursor = db.cursor()
cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
for data in cursor.fetchall():
#    if data[1][0] == 'N':
    print (data)
db.close()
