# Exercise 47 - Conditioned Letter Extractor
import glob

dir_name = 'letters'
test_word = 'python'

letters = []
file_list = glob.glob(dir_name + '/*.txt')

for filename in file_list:
	with open(filename, 'r') as f:
		letter = f.read().strip('\n')
		if letter in test_word:
			letters.append(letter)

print(sorted(letters))