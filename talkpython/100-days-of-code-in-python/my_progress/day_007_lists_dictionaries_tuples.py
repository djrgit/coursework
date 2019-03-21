#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Lists
print('\n'*2)
print('Working with lists: ')
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


# Tuples
print('\n'*2)
print('Working with tuples: ')
lst1.pop()
lst1.insert(len(lst1), 'tuple')
tup1 = tuple(lst1)
print(tup1)
lst2 = lst2[:-4]
lst2.extend(list('tuple'))
tup2 = tuple(lst2)
print(tup2)

print(tup1[0])
print(tup2[0])


# Dictionaries
print('\n'*2)
print('Working with dictionaries: ')
conf_mgmt_tools = {'Puppet':'client-server',
                   'Chef':'client-server',
                   'Ansible':'ssh',
                   'SaltStack':'client-server'}
print(conf_mgmt_tools['Ansible'])

print(conf_mgmt_tools.keys())
print(conf_mgmt_tools.values())

for keys, values in conf_mgmt_tools.items():
    print(keys, values)
