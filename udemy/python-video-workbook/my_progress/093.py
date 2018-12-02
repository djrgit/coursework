# Exercise 93 - Recursive File Counter
import os

directory = './subdirs'

num_py = 0
for root, dirs, files in os.walk(directory):
	num_py += len([file for file in files if file.endswith('.py')])
print(num_py)

'''
# ALTERNATIVE SOLUTION
import glob
 
file_list = glob.glob("subdirs/**/*.py", recursive=True)
print(len(file_list))
'''