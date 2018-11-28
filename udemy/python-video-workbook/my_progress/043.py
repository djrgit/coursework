# Exercise 43 - Letters Two by Two
import string

with open('letters_2x2.txt', 'w') as f:
	for l1, l2 in zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2]):
		f.write(l1 + l2 + '\n')