import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


# database = '/Users/matthardy/opt/sqlite/data/embedded.db'
database = '../sqlite/embedded.db'
sql_create_merit_table = """CREATE TABLE IF NOT EXISTS tblMerit (
    pkMeritID integer PRIMARY KEY,
    merit integer,
    demerit integer null,
    dateof TEXT NOT NULL,
    fkEmployeeID INTEGER NOT NULL,
    FOREIGN KEY (fkEmployeeID) REFERENCES tblEmployee (pkEmployeeID)
);"""

sql_create_employee_table = """CREATE TABLE IF NOT EXISTS tblEmployee (
    pkEmployeeID integer PRIMARY KEY,
    firstName TEXT,
    lastName TEXT,    
    title TEXT,
    email TEXT
);"""


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_employee(conn, employee):
    sql = '''INSERT INTO tblEmployee(firstName, lastName, title, email)
            VALUES(?, ?, ?, ?)'''
    cursor = conn.cursor()
    cursor.execute(sql, employee)
    conn.commit()
    return cursor.lastrowid


def create_merit(conn, merit):
    sql = '''INSERT INTO tblMerit(merit, demerit, dateof, employeeID)
            VALUES(?, ?, ?)'''
    cursor = conn.cursor()
    cursor.execute(sql, merit)
    conn.commit()
    return cursor.lastrowid
