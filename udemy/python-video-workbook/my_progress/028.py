# Exercise 28 - TypeError
def foo(a, b):
	# print(a + b) # Doesn't return anything from function, causing error when called
    return (a + b) # Fixed
     
x = foo(2, 3) * 10
print(x)