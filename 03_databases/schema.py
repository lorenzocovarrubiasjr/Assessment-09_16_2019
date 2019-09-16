import sqlite3
import os 

DIR = os.path.dirname(__file__)
DBPATH = os.path.join(DIR, 'organization.db')

def schema(dbpath=DBPATH):
    with sqlite3.connect(dbpath) as conn:
        curs = conn.cursor()
    
        SQL = "DROP TABLE IF EXISTS branches;"
        curs.execute(SQL)

        SQL = """ CREATE TABLE branches (
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                city VARCHAR(128),
                state VARCHAR(128),
                zip_code INTEGER
        );"""
        curs.execute(SQL)

        SQL = "DROP TABLE IF EXISTS employees;"
        curs.execute(SQL)

        SQL = """ CREATE TABLE employees (
                pk INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name VARCHAR(128),
                last_name VARCHAR(128),
                employee_id VARCHAR(128),
                salary FLOAT,
                branch_id INTEGER,
                FOREIGN KEY(branch_id) REFERENCES branches(pk) ON DELETE CASCADE
            ON UPDATE CASCADE
        );"""
        curs.execute(SQL)
        
schema()