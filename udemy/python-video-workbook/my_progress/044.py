# Exercise 44 - Letters Three by Three
import string

group = 3
letters = string.ascii_lowercase

while len(letters) % group != 0:
	letters += ' '

with open('letters_3x3.txt', 'w') as f:
	for l1, l2, l3 in zip(letters[0::3], letters[1::3], letters[2::3]):
		f.write(l1 + l2 + l3 + '\n')