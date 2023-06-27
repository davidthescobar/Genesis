# Enumerate

# This prints the index number with the iterable object
for i,char in enumerate('hello'):
  print(i,char)

# print(list(range(100)))

for i,char in enumerate(list(range(100))):
  if char == 50:
    print(f'The index of 50 is {i}')