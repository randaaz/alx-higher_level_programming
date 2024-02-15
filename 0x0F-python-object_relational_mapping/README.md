# 0x0F. Python - Object-relational mapping

## Description
This project explores the world of Object-Relational Mapping (ORM) in Python, connecting databases and Python through modules like MySQLdb and SQLAlchemy. It focuses on using ORM to abstract the storage layer, making Python code interact with databases without directly writing SQL queries.

## Prerequisites
Before you start, ensure that your MySQL server is in version 8.0. You can refer to [How to install MySQL 8.0 in Ubuntu 20.04](https://example.com) for installation instructions.

## Background Context
In this project, you will link the worlds of Databases and Python using Object-Relational Mapping (ORM). The key aspect is to abstract storage, allowing you to interact with objects rather than writing direct SQL queries.

## Tasks
- 14 mandatory tasks
- 3 advanced tasks

### Without ORM:
```python
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()

### With ORM:

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
session.close()
