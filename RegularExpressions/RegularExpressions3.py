# Regular Expressions are useful for validation
import re


# regex101.com
# The regex below reads: "Any letter a-Z > ant character > the letter a"
pattern =re.compile(r"(^\S+@\S+\.\S+$)") # the 'r' stands for raw string
string = 'b@o.com'

a = pattern.search(string)
print(a)
# print(a.start())
# print(a.end())
# print(a.group())