# Exercise 97 - Advanced File Writer
file = 'user_data_save_close.txt'
entries = []

def submit_text():
	entry = input('Write a value: ')
	return entry

def save(entries, file):
	with open(file, 'a+') as f:
		for e in entries:
			f.write(e + '\n')
	entries = []
	return entries

def close(entries, file):
	save(entries, file)

while True:
	entry = submit_text()
	if entry != 'SAVE' and entry != 'CLOSE':
		entries.append(entry)
	elif entry == 'SAVE':
		entries = save(entries, file)
	elif entry == 'CLOSE':
		close(entries, file)
		break