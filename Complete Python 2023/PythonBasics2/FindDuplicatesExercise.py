# Exercise: Check for duplicates in a list
my_list = ['a','b','c','b','d','m','n','n']

# Iterate through list
# Set variable equal to duplicates
# Print variables

new_list = []
duplicates = []

for value in my_list:
  if my_list.count(value) > 1:
    duplicates.append(value)

print(duplicates)



# for i in my_list:
#   if i not in new_list:
#     new_list.append(i)
#   else:
#     duplicates.append(i)

# print(duplicates)