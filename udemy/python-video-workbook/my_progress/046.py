# Exercise 46 - Letter Extractor
import os
# Could also use glob

dir_name = 'letters'

def build_list(dir):
	lst = []
	for root, dirs, files in os.walk('./' + dir_name):
		for file in files:
			with open('./' + dir_name + '/' + file, 'r') as f:
				for line in f:
					lst.append(line.strip())
	lst = sorted(lst)
	return lst

print(build_list(dir_name))

'''
ALTERNATE SOLUTION
import glob

letters = []
file_list = glob.glob('letters/*.txt')

for filename in file_list:
	with open(filename, 'r') as f:
		letters.append(file.read().strip('\n'))

print(letters)
'''