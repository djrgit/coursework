# Exercise 74 - File Concatenator
import pandas as pd

url1 = 'http://www.pythonhow.com/data/sampledata.txt'
url2 = 'http://www.pythonhow.com/data/sampledata_x_2.txt'

data = pd.concat([pd.read_csv(url1), pd.read_csv(url2)])
data.to_csv('sampledata_concat.txt', index=False)