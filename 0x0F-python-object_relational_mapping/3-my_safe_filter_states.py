#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves records
from the 'states' table based on a provided state name pattern.
It takes fivecommand-line arguments:
<username>, <password>, <database>, <state_name_pattern>, and <charset>.
The script queries the 'states' table for records whose 'name'
column matches the provided pattern using a parameterized query.
It prints the details of the matching states,
ordered by ID in ascending order.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                        passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                   (argv[4],))
    rws = cursor.fetchall()
    for rw in rws:
        print(rw)
    cursor.close()
    db.close()
