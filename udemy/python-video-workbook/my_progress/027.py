# Exercise 27 - Acceleration Calculator
import sys

v1, v2, t1, t2 = sys.argv[1:]

def acceleration(v1, v2, t1, t2):
	return (v2-v1)/(t2-t1)

print(acceleration(int(v1), int(v2), int(t1), int(t2)))