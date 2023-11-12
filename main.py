import pandas as pd
import db.create_db as db
import sqlalchemy as sql


if __name__ == '__main__':

    conn = sql.create_engine('sqlite:///sqlite/embedded.db').connect()
    df = pd.read_sql('select * from tblEmployee', conn)
    print(df)
    # df = pd.read_sql_table('tblEmployee', conn)
    # print(df)

    # conn = db.create_connection('sqlite/embedded.db')

    # if conn is not None:
    #     table_name = 'tblEmployee'
    #     engine = sql.create_engine(conn)
    #     df = pd.read_sql_table(table_name, engine)
    #     print(df)
    # else:
    #     print("ERROR WILL ROBINSON. Unable to create database table")
