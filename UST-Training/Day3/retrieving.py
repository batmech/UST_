import sqlite3

"""
The Code is the implementation of fetchall and
fetchone which are methods of cursor object in sqlite
"""

dbCon = sqlite3.connect('Tutorial.db')
cur = dbCon.cursor()

try:
    cur.execute('SELECT * FROM TESTING')
    data = cur.fetchone()
    print('PID\tName\tAge')
    print(*data, sep='\t')
    data = cur.fetchall()
    for elem in data:
        print(*elem, sep='\t')

except Exception as e:
    print('Error: ', e)
