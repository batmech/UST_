from os import sep
import sqlite3

dbCon = sqlite3.connect('Tutorial.db')

cur = dbCon.cursor()

cur.execute(
    """
    SELECT PID,NAME,MAX(AGE) AS OLDEST
    FROM TESTING
    """
)

data = cur.fetchall()

for item in data:
    print(*item, sep='\t')

dbCon.commit()
dbCon.close()