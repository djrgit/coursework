#!/usr/bin/python

import os

for root, dirs, files in os.walk("."):
	for file in files:
		directory = os.path.split(root)[-1]
		if not file.endswith('checkpoint.ipynb') and file.endswith('.ipynb'):
			#file_name = os.path.join(directory, file)
			#print(file_name)
			src = os.path.join(root, file)
			print(src)
			os.rename(src, src.replace(' ', '_'))