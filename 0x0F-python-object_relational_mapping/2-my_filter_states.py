#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves
records from the 'states' table based on a provided state name pattern.
It takes four command-line
arguments: <username>, <password>, <database>, and <state_name_pattern>.
The script queries the 'states' table
for records whose 'name' column matches the provided pattern.
It prints the details of the matching states,
ordered by ID in ascending order.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    d = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost",
                        passwd=sys.argv[2], d=sys.argv[3])
    s = d.cursor()
    s.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(sys.argv[4]))
    states = s.fetchall()
    for t in states:
        if t[1] == sys.argv[4]:
            print(t)
    s.close()
    d.close()
