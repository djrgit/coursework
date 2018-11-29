# Exercise 71 - Letter Counter
import requests

response = requests.get('http://www.pythonhow.com/data/universe.txt')
print(response.text.count('a'))
