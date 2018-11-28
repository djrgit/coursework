# Exercise 24 - Iterate Dictionary
d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

for key, vals in d.items():
	print('{} has value {}'.format(key, vals))