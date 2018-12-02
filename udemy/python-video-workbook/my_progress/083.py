# Exercise 83 - Monitor Size Detector
import screeninfo

monitors = screeninfo.get_monitors()

for i, monitor in enumerate(monitors):
	print("Monitor " + str(i + 1) + ": ")
	print("Width: {}, Height: {}".format(monitor.width, monitor.height))
	print('\n')