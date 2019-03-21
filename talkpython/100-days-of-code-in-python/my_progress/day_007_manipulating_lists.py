#! /usr/bin/env python
# -*- coding: utf-8 -*-

lst1 = 'This is a list'.split()
lst2 = list('This is also a list')

print(lst1)
print(lst2)

numlist = list(range(1,6))
print(numlist)
numlist.reverse()
print(numlist)
numlist.reverse()
numlist.sort()
print(numlist)

for num in numlist:
    print(str(num))

str1 = ' '.join(lst1)

lst1.pop()
lst1.insert(len(lst1), 'string')
str1 = ' '.join(lst1)
print(str1)
