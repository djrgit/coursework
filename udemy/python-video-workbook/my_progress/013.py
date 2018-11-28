# Exercise 13 - Ranges of Strings
my_range = range(1, 21)

def convert_ints_to_strs(parameter1):
	return list(map(str, my_range))

print(convert_ints_to_strs(my_range))