# Exercise 86 - Data Checker
checklist = ["Portugal", "Germany", "Munster", "Spain"]

with open('countries_clean.txt', 'r') as f:
	countries = [l.strip('\n') for l in f.readlines()]
	filtered = [c for c in checklist if c in countries]
	print(sorted(filtered))