# Range is a object that returns an object which producers a sequence of integers from start to stop

print(range(0,100))

for _ in range(0, 10, 2):
  print(_)

for _ in range(10, 0, -2):
  print(_)

for _ in range(2):
  print(list(range(10)))

for number in range(0, 101):
  print(number)