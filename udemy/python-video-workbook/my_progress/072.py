# Exercise 72 - Google Searcher
import webbrowser

query = input('Enter your Google query: ')
url = 'https://www.google.com/search?q={}'.format(query)
webbrowser.open_new_tab(url)