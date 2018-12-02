# Exercise 88 - Data Filter
import pandas as pd

countries_by_area = pd.read_csv('countries_by_area.txt')
countries_by_area['pop_density'] = countries_by_area['population_2013'] /\
 								   countries_by_area['area_sqkm']
top_5_pop_density = countries_by_area.nlargest(5, 'pop_density')['country']

for i in top_5_pop_density:
	print(i)