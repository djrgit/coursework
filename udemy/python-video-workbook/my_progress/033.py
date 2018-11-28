# Exercise 33 - Local Variables
c = 1
def foo():
	c = 2
	return c
c = 3
print(foo())