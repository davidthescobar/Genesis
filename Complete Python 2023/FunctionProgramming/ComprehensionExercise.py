# Exercise: Check for duplicates with comprehension
my_list = ['a','b','c','b','d','m','n','n']

# Iterate through list
# Set variable equal to duplicates
# Print variables

duplicates = []

duplicates2 = {duplicates.append(v) for v in my_list
              if my_list.count(v) > 1 and v not in duplicates}

print(duplicates)