import sqlite3
import random

db = sqlite3.connect('Tutorial.db')
cur = db.cursor()

cur.execute("""CREATE TABLE TESTING (\
        PID INTEGER PRIMARY KEY AUTOINCREMENT,\
        NAME VARCHAR (10),
        AGE INT
        )"""
    )

names = [name.strip() for name in input('Enter names:').split(',')]
ages = [random.randint(18,35) for _ in names]

for ind in range(len(names)):
    if len(names[ind]) < 10:
        cur.execute(
            """INSERT INTO TESTING
            (Name,Age) VALUES (?,?)"""
            ,(names[ind],ages[ind]
        ))

db.commit()
db.close()