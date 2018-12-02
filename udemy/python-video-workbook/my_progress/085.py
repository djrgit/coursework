# Exercise 85 - Data Cleaner
countries = []
with open('countries_raw.txt', 'r') as f:
	for line in f:
		if len(line) <= 2 or 'Top of Page' in line:
			pass
		else:
			countries.append(line.strip('\n'))

with open('countries_clean.txt', 'w') as f:
	for i in countries:
		f.write(i + '\n')