import os

def build_list():
	lst = []
	for root, dirs, files in os.walk('.'):
		for file in files:
			if file[0:3].isdigit():
				with open(file, 'r') as f:
					first = f.readlines(0)
					lst.append(file[0:3] + ' - ' + first[0])
	lst = sorted(lst)
	return lst

with open('exercise_descriptions.txt', 'w') as file:
	for item in build_list():
		print(item.strip())
		file.write(item.strip() + '\n')