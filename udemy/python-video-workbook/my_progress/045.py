# Exercise 45 - One File per Letter
import os
import string

dir_name = 'letters'

if not os.path.exists(dir_name):
	os.makedirs(dir_name)

for letter in string.ascii_lowercase:
	with open(dir_name + '/' + letter +'.txt', 'w') as f:
		f.write(letter + '\n')