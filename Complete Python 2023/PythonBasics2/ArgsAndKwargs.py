# *args lets us use as many arguments as we want stored into a tuple
# **kwargs lets us use as many keyword arguments as we want stored into a dictionary

# Parameter rules: params, *args, default param, **kwargs
# def example (name, *args, lastname='N/A', **kwargs)

def super_fun (*args, **kwargs):
  total = 0
  for items in kwargs.values():
    total += items
  return sum(args) + total

print(super_fun(1,2,3,4,5, num1=5, num2=10))