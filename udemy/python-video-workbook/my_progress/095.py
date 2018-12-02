# Exercise 95 - Comma Separated Input
values = input('Enter values separated by commas : ')
file = 'user_data_commas.txt'

with open(file, 'a+') as f:
	val_lst = [val.strip() for val in values.split(',')]
	for v in val_lst:
		f.write(v + '\n')