# Exercise 96 - File Writer
entry = None
while entry != 'CLOSE':
	with open('user_data.txt', 'a+') as f:
		if entry:
			f.write(entry + '\n')
	entry = input('Write a value: ')