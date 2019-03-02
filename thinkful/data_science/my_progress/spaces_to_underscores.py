#!/usr/bin/python

import os

for root, dirs, files in os.walk("."):
	for file in files:
		directory = os.path.split(root)[-1]
		if not file.endswith('checkpoint.ipynb') and file.endswith('.ipynb'):
			src = os.path.join(root, file)
			os.rename(src, src.replace(' ', '_'))