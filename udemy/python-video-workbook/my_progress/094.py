# Exercise 94 - URL Cleaner
file = 'urls.txt'

with open(file, 'r+') as f:
	lines = []
	for line in f:
		if line.startswith('https:/'):
			line = line.replace('https:/', 'http://')
		lines.append(line)
	f.seek(0)
	for line in lines:
		f.write(line)
	f.truncate()