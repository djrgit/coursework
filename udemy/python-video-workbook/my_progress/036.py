# Exercise 36 - Word Counter
import sys

file = sys.argv[1]

def word_counter(file):
	total = 0
	if file.endswith('txt'):
		with open(file, 'r') as f:
			for line in f:
				total += len(line.split())
	return total

print(word_counter(file))