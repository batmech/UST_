from os import sep
import sqlite3
import random

names = ['Allwyn', 'Bat', 'Thomas',
         'Nibu', 'James', 'Bond', 'Asma', 'Devika']
subject = ['Maths', 'Computers', 'Physics', 'Chemistry']

dbCon = sqlite3.connect('Tutorial.db')
cur = dbCon.cursor()
cur.execute("""
            CREATE TABLE BOOKTEST 
            (PID INTEGER PRIMARY KEY, 
            NAME VARCHAR(20),
            SUBJECT VARCHAR (20)
            )
            """)

for name in names:
    cur.execute("""
                INSERT INTO BOOKTEST (NAME,SUBJECT)
                VALUES (?,?)
                """, (name, random.choice(subject))
                )
print('-----------------TESTING TABLE----------------')
cur.execute('''
            SELECT * FROM TESTING t
        ''')
data = cur.fetchall()
for item in data:
    print(*item, sep='\t')

print('-----------------BOOKTEST TABLE----------------')
    
cur.execute('''
            SELECT * FROM BOOKTEST t
        ''')
data = cur.fetchall()
for item in data:
    print(*item, sep='\t')

print('-----------------INNER JOIN TABLE----------------')

cur.execute("""
            SELECT * FROM TESTING t LEFT JOIN
            BOOKTEST b ON t.PID = b.PID
            """)
data = cur.fetchall()
for item in data:
    print(*item, sep='\t')

dbCon.commit()
dbCon.close()