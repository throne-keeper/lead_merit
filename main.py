import pandas as pd
import db.create_db as db
import sqlalchemy as sql
from db import employee as emp


if __name__ == '__main__':

    conn = sql.create_engine('sqlite:///sqlite/embedded.db').connect()
    df = pd.read_sql('select * from tblEmployee', conn)
    employees = list()
    for i,v in df.iterrows():
        values = v.values
        newEmp = emp.Employee(values[0], values[1], values[2], values[3], values[4])
        employees.append(newEmp)

    for emp in employees:
        print(repr(emp))