# Understanding Data Structures

# A dictionary is not sorted, but can hold more information
# A list has order

# If you have a line of people at your store, you should probably use an ordered list.

# If you have a user play a game, they might have many unrelated data types like a name, weapons, pets, etc. that don't make sense to order. A dictionary might be a good fit in this case.

dict

# Un-ordered Key & Value pair
dictionary = {
  'a': [1,2,3],
  'x': 'hello',
  'b': True
}

print(dictionary['a'][1])

my_list = [
  {
  'a': [1,2,3],
  'x': 'hello',
  'b': True
  },
  {
  'a': [4,5,6],
  'x': 'hello',
  'b': True
  }
]

print(my_list[0]['a'][2])