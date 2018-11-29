# Exercise 75 - Data Plotter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

url1 = 'http://www.pythonhow.com/data/sampledata.txt'

data = pd.read_csv(url1)
sns.scatterplot(x='x', y='y', data=data)
plt.show()

'''
# ALTERNATE SOLUTION
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas
 
output_file("bokeh_plot.html")
data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
f = figure()
f.circle(x=data["x"], y=data["y"])
 
show(f)
'''