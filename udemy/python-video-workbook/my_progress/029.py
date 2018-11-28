# Exercise 29 - Liquid Volume Calculator
import math
import sys

# https://www.1728.org/spherprt.gif
h_cap_height = sys.argv[1]
RADIUS = 10

def liquid_volume_in_sphere(R, hc):
	return (((4*math.pi*(R**3))/3) - ((math.pi*(hc**2)*((3*R)-hc))/3))

print(liquid_volume_in_sphere(RADIUS, int(h_cap_height)))