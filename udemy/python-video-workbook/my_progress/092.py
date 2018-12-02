# Exercise 92 - File Counter
import os

directory = './files'

for root, dirs, files in os.walk(directory):
	num_py = len([file for file in files if file.endswith('.py')])
print(num_py)

'''
# ALTERNATIVE SOLUTION
import glob
 
file_list=glob.glob1("files","*.py")
print(len(file_list))
'''