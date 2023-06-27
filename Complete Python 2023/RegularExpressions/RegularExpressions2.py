# Regular Expressions are useful for validation
import re


# regex101.com
# The regex below reads: "Any letter a-Z > ant character > the letter a"
pattern =re.compile(r"([a-zA-Z]).([a])") # the 'r' stands for raw string
string = 'Search this inside of this text please'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print(a.group())
print(a.group(1))
print(a.group(2))
print(d)
# print(a.start())
# print(a.end())
# print(a.group())