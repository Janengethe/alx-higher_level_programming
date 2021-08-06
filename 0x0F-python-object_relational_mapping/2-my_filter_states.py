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
sqry ="""SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC""".format(argv[4])
cursor.execute(sqry)
for data in cursor.fetchall():
    print (data)
db.close()
