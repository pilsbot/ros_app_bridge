
import sqlite3

database_path = "../database/database.db"

def select_one(table):
    db =  sqlite3.connect(database_path)
    sql = "SELECT * FROM "+table
    cur = db.cursor()
    cur.execute(sql, [])
    resp = cur.fetchall()
    return resp[0][0]

def overwrite_one(table, value):
    db = sqlite3.connect(database_path)
    sql = "DELETE FROM "+table
    db.cursor().execute(sql, [])
    sql = "INSERT INTO "+table+" VALUES (?) "
    db.cursor().execute(sql, [value])
    resp = db.cursor().fetchall()
    db.commit()
