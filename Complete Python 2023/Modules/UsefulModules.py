# These modules are useful

# The names with capital letters are classes
# The name with lowercase letters are functions
from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7]
sentence = 'hello'
# Counter populates a dictionary with reacurring items
print(Counter(li))
print(Counter(sentence))


# deafaultdict lets us specify a default value when items that don't exist
dictionary = defaultdict (lambda: 'fake',{'a': 1, 'b': 2})
print(dictionary['c'])

# OrderedDict retains the order of the created dictionary
# AFTER PYTHON 7, DICTIONARIES ARE ORDERED BY DEFAULT

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d == d2)