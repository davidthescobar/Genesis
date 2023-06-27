
# map, filter, zip, reduce
from functools import reduce

my_list = [1,2,3]
your_list = [10,20,30]

def multiply_by2(item):
  return item*2

def check_odd(item):
  return item % 2 != 0

def accumulator(acc, item):
  return acc + item

print(list(map(multiply_by2, my_list)))
print(list(filter(check_odd, my_list)))
print(list(zip(my_list, your_list)))

print('test')
print(reduce(accumulator, my_list, 0))