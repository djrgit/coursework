# Exercise 32 - Global Variables
c = 1
def foo():
    return c
c = 3
print(foo())