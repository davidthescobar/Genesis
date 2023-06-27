# Pure functions;
# 1 - given the same input, it will always return the same output
# 2 - a function should not produce side-effects/interact with the outside world

# Pure
def times_two(li):
  new_list = []
  for i in li:
    new_list.append(i*2)
  return new_list


print(times_two([1,2,3]))


# Not pure
def times_two2(li):
  new_list = []
  for i in li:
    new_list.append(i*2)
  print(new_list)


times_two2([1,2,3])


# Not pure
new_list = []
def times_two3(li):
  for i in li:
    new_list.append(i*2)
  return new_list


print(times_two([1,2,3]))