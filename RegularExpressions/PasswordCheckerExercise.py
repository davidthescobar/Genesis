# Create a password checker using regex
# input at least 8 characters long
# contain any letters, numbers, or $%#@
import re

pattern = re.compile(r"[A-Za-z@#$%0-9]{8,}\d")
password = str(input('Create a password at least 8 characters long containing letters, numbers, or $%#@: '))

a = pattern.search(password)
# print(a.group())
try:
  if a.group() == password:
    print(f'Your password is {password} and meets all the requirements')
  else:
    print('Password must end with a number')
except AttributeError as e:
  print(f'\'{password}\' must be at least 8 characters long')