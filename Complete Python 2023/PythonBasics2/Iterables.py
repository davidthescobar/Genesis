# Iterable is an object or collection that can be iterated over
# list, tuple, set, dictionary, string
# iterated means going 1 by 1 to check each item in the collection

user = {
  'name': 'Golem',
  'age': 5006,
  'can_swim': False
}

for k, v in user.items():
  print(k, v)

for item in user.items():
  print(item)

for item in user.values():
  print(item)

for item in user.keys():
  print(item)