# Dictionary

user = {
  'basket': [1,2,3],
  'greet': 'hello',
  'age': 20
}


print(user.items())
print('age' in user)
print('basket' in user.keys())
print('hello' in user.values())

print(user.update({'age': 55}))
print(user)

user.pop('age')
print(user)

print('debug')

print(user.popitem())
print(user)


user_2 = user.copy()
user.clear()
print(user)
print(user_2)