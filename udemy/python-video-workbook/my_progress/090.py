# Exercise 90 - Database to CSV Converter
import pandas as pd
import sqlite3

conn = sqlite3.connect('database.db')
query = "SELECT * FROM countries WHERE area >= 2000000"
df = pd.read_sql_query(query, conn)
conn.close()

df = df.rename(columns={'id': 'rank'})
df.columns = [c.capitalize() for c in df.columns]
df.set_index('Rank', inplace=True)
df.to_csv('countries_big_area.csv')