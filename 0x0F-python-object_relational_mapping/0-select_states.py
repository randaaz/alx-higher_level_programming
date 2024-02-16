#!/usr/bin/python3
"""
A script to connect to a MySQL database and
retrieve records from the 'states' table.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    s = db.cursor()
    s.execute("SELECT * FROM `states`")
    [print(state) for state in s.fetchall()]
