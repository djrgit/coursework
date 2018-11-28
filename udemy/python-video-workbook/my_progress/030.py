# Exercise 30 - Arguments
def foo(b, a=2): # Non-default parameters should come before default parameters
	return a + b

print(foo(3))