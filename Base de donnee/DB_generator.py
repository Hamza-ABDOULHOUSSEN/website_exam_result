import sqlite3

DATABASE = "CMT_database.db"
conn = sqlite3.connect(DATABASE)
c = conn.cursor()

with open("../Schéma Relationnel/database.sql") as file:
    content = file.read().split("\n")
    command = ""
    for line in content:
        if line.endswith(";"):
            command += line.strip()
            c.execute(command)
            command = ""
        else:
            command += line.strip()

conn.commit()
conn.close()
