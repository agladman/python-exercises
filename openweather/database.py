import sqlite3


def connect():
    "connect to database and return connection object"
    return sqlite3.connect("airquality.db")

def create_table(connection):
    "creates the records table if it doesn't exist"
    with connection:
        connection.execute("""CREATE TABLE IF NOT EXISTS records (
                            record_id INTEGER PRIMARY KEY,
                            aqi INTEGER,
                            co REAL,
                            no REAL,
                            no2 REAL,
                            o3 REAL,
                            so2 REAL,
                            pm2_5 REAL,
                            pm10 REAL,
                            nh3 REAL,
                            dt TIMESTAMP)""")

def add_record(connection, args):
    "adds a record to the database"
    with connection:
        connection.execute("""INSERT INTO records(
            aqi, co, no, no2, o3, so2, pm2_5, pm10, nh3, dt) 
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", args)
