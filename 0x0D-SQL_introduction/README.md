# 0x0D. SQL - Introduction

## Concepts
For this project, we expect you to explore the following concepts:

- Databases
- What is a Database & SQL?
- A Basic MySQL Tutorial
- Basic SQL statements: DDL and DML (no need to read the chapter “Privileges”)
- Basic queries: SQL and RA
- SQL technique: functions
- SQL technique: subqueries
- What makes the big difference between a backtick and an apostrophe?
- MySQL Cheat Sheet
- MySQL 8.0 SQL Statement Syntax
- Installing MySQL in Ubuntu 20.04

## Learning Objectives
By the end of this project, you should be able to explain to anyone, without the help of Google:

### General
- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries
- How to use MySQL functions

## Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks yourself.
- Do not copy and paste someone else’s work.
- No content of this project is allowed to be published.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start with a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

## More Info
### Comments for your SQL file:
```bash
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

## Tasks
- 16 mandatory
- 4 advanced
