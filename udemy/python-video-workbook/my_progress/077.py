# Exercise 77 - Year of Birth Calculator
from datetime import datetime

age = int(input('Enter your age: '))
birth_year = datetime.now().year - age
print('We think you were born back in {}'.format(birth_year))