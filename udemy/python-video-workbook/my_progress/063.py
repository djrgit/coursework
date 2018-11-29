# Exercise 63 - Progressive Time Printer with Threshold
import time

t = 0

while t < 4:
	time.sleep(t)
	print('Hello')
	t += 1

print('End of Loop')


'''
ALTERNATE SOLUTION
import time

t = 0
while True:
	t += 1
	if t > 3:
		print('End of Loop')
		break
	time.sleep(t)
'''