#!/usr/bin/python3
"""
A script to connect to a MySQL database and
retrieve records from the 'states' table.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    dtb = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], dtb=sys.argv[3])
    s = dtb.cursor()
    s.execute("SELECT * FROM `states`")
    [print(state) for state in s.fetchall()]
