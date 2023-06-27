# Regular Expressions are useful for validation
import re


pattern =re.compile('this')
string = 'Search this inside of this text please'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(a)
print(b)
print(c)
print(d)
# print(a.start())
# print(a.end())
# print(a.group())