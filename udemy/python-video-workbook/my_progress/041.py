# Exercise 41 - Letters in File
import string

with open('alphabet.txt', 'w') as f:
	for char in string.ascii_lowercase:
		f.write(char + '\n')