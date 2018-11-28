# Exercise 14 - Removing Duplicates

# Answer 1
a = ["1", 1, "1", 2]
a = list(set(a))
print(a)

# Answer 2
from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)