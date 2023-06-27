# Tuple
# Tuples are like lists, but they are immutable - means you can't change
# Think of them as immutable lists
# You can't sort them, reverse them, etc.

my_tuple = (1,2,3,4,5)
print(my_tuple[1])
print(5 in my_tuple)

# my_tuple[1] = 'z'


user = {
  (1,2): [1,2,3],
  'greet': 'hello',
  'age': 20
}

print(user[1,2])
print(user.items()) # This prints the dictionary as a tuple!