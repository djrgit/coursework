# Exercise 12 - More Ranges
my_range = range(1, 21)

def x10(parameter1):
	return [x * 10 for x in my_range]

print(x10(my_range))