#!/usr/bin/python3
"""
module to list all states from database hbtn_0e_0_usa
"""
import MySQLdb

db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="gokuaddicte22",
    port=3306,
    db="hbtn_0e_0_usa")
cur = db.cursor()

cur.execute("SELECT * FROM states ORDER BY states.id")
rows = cur.fetchall()
for row in rows:
    print(row)
