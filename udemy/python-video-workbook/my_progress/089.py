# Exercise 89 - Database Filter
import sqlite3

conn_obj = 'database.db'
conn = sqlite3.connect(conn_obj)
c = conn.cursor()

query = "SELECT * FROM countries WHERE area >= 2000000"

for row in c.execute(query):
	print(row[1])

conn.close()


'''
# ALTERNATE SOLUTION
import sqlite3

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("SELECT country FROM countries WHERE area >= 2000000")
rows = cur.fetchall()
conn.close()

for i in rows:
	print(i[0])
'''