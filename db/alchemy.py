import sqlalchemy as db;
import sqlite

engine = db.create_engine('sqlite:////Users/matthardy/opt/sqlite/data/embedded.db')
connection = engine.connect()
metadata = db.MetaData()
employee = db.Table('tblEmployee', metadata, autoload_with=engine)

if __name__ == '__main__':
    query = db.select([employee])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()
    ResultSet[:3]
