#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from collections import namedtuple
from collections import Counter
from collections import deque
import csv
import random
import timeit
from urllib.request import urlretrieve


# namedtuple example - defining a class without methods
Country = namedtuple('Country', 'name capital')
country = Country(name='USA', capital='Washington, D.C.')

print('\nnamedtuple example: ')
print('\t', country.name)
print('\t', country.capital)
print('\t', f'{country.name} has {country.capital} as its capital.')


# defaultdict example
groceries_purchased = [('apple', 5), ('orange', 7), ('banana', 4),
                       ('apple', 3), ('pear', 2), ('tomato', 1), ('banana', 2)]

groceries = defaultdict(list)
for item, qty in groceries_purchased:
    groceries[item].append(qty)  # item may not yet exist in data structure;
    							 # inserts qty into defaultdict along with item

print('\ndefaultdict example: ')
print('\t', groceries_purchased)
print('\t', groceries)


# Counter example
# https://www.goodreads.com/author/quotes/4918776.Seneca
words = """The time will come when diligent research over long periods will bring to light things which now lie hidden. A single lifetime, even though entirely devoted to the sky, would not be enough for the investigation of so vast a subject... And so this knowledge will be unfolded only through long successive ages. There will come a time when our descendants will be amazed that we did not know things that are so plain to them... Many discoveries are reserved for ages still to come, when memory of us will have been effaced. ― Seneca, Natural Questions""".split()

print('\nCounter example: ')
print('\t', words)
print('\t', Counter(words).most_common(5))


# deque example
my_setup = """
from collections import deque
import random

lst = list(range(5000000))
deq = deque(range(5000000))

def insert_and_delete(items):
    for _ in range(10):
        index = random.choice(range(500))
        items.remove(index)
        items.insert(index, index)
"""

print('\ndeque example (100 iterations for list and deque): ')
print('\ttime for list:  ', timeit.timeit(stmt="insert_and_delete(lst)", 
    setup=my_setup, number=100))
print('\ttime for deque: ', timeit.timeit(stmt="insert_and_delete(deq)", 
    setup=my_setup, number=100))

