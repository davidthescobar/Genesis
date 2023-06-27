# Create a function that takes a number as the index number of fibonaci
# This is a generator and will not take up any storage
def fib(num):
  a = 0
  b = 1
  for i in range(num):
    yield a
    temp = a
    a = b
    b = temp + a



for x in fib(10000):
  print(x)




# This is not a generator and will use storage -> less efficient
def fib2(num):
  a = 0
  b = 1
  result = []
  for i in range(num):
    result.append(a)
    temp = a
    a = b
    b = temp + a
  return result

# print(fib2(10000))