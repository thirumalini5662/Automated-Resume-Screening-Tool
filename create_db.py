import sqlite3

con = sqlite3.connect("db/screening.db")

with open("schema.sql", "r") as f:
    con.executescript(f.read())

con.commit()
con.close()

print("Database created successfully!")