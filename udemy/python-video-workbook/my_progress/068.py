# Exercise 68 - User Friendly Translator
d = dict(weather = "clima", earth = "terra", rain = "chuva")

def vocabulary(word):
	try:
		return d[word.casefold()]
	except KeyError:
		return "We couldn't find that word!"

word = input('Enter word: ')
print(vocabulary(word))