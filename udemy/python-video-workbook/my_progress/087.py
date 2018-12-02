# Exercise 87 - Add Missing Data
checklist = ['Portugal', 'Germany', 'Spain']

with open('countries_missing.txt', 'r+') as f:
	countries = [l.strip('\n') for l in f.readlines()]
	countries = countries + [c for c in checklist if c not in countries]
	countries = sorted(countries)
	f.seek(0)
	for i in countries:
		f.write(i + '\n')
	f.truncate()