# Exercise 91 - CSV to Database
import pandas as pd
import sqlite3

csv = 'ten-more-countries.txt'
db = 'database.db'
data = pd.read_csv(csv)

conn = sqlite3.connect(db)
c = conn.cursor()
query = """INSERT INTO countries (id, country, area) VALUES (?,?,?)"""

for index, row in data.iterrows():
	c.execute(query, tuple(row))

conn.commit()
conn.close()