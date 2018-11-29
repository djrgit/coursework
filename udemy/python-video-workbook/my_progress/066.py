# Exercise 66 - Translator
d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocabulary(word):
	return d[word] if word in d else ''

word = input('Enter word: ')
print(vocabulary(word))