# Exercise 73 - Data Multiplier
import pandas as pd

url = 'http://www.pythonhow.com/data/sampledata.txt'
data = pd.read_csv(url)
data_x2 = data * 2
data_x2.to_csv('sampledata_x2.txt', index=False)