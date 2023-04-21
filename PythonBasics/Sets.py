# Sets
# Unordered collections of unique objects!
# They do not support indexing

my_list = [1,2,3,4,5,5]
print(set(my_list)) # Prints a new set out of a list, meaning no duplicates!
my_set = {1,2,3,4,5,5}
print(my_set) # In a set, there are no duplicates. Only unique values are returned
my_set.add(100)
my_set.add(2)
print(my_set)



# Syntax for declaring a list, tuple, and set:
# List: []
# Tuple: ()
# Set: {}