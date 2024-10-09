import sqlite3

conn =sqlite3.connect('Tutorial.db')
cur = conn.cursor()

# UPDATING QUERIES
userID = int(input('Enter ID: '))
updateAge = int(input('Enter age to be updated: '))
cur.execute("""
            UPDATE TESTING
            SET AGE = (?)
            WHERE PID = (?)
            """, (updateAge,userID)
        )

# RETRIEVING
cur.execute('SELECT * FROM TESTING')
data = cur.fetchall()
print("""PID\tNAME\tAGE""")
for item in data:
    for elem in item:
        print(elem, end='\t')
    print()

# DELETING
userID = int(input('Enter user ID: '))
cur.execute("""
            DELETE FROM TESTING
            WHERE PID = (?)
            """, (userID,)
            )

conn.commit()
conn.close()