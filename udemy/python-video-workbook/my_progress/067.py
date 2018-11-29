# Exercise 67 - Advanced Translator

d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocabulary(word):
	return d[word] if word in d else "We couldn't find that word!"

word = input('Enter word: ')
print(vocabulary(word))


'''
# ALTERNATE SOLUTION
d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocabulary(word):
	try:
		return d[word]
	except KeyError:
		return "We couldn't find that word!"

word = input('Enter word: ')
print(vocabulary(word))
'''