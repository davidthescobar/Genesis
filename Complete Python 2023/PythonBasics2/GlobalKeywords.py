
# Accessing global keywords insie a function - use "global"
total = 0

def count():
  global total 
  total += 1
  return total
print(count())

# BUT! Dependency Injection is a better way to access gobal variables.
# To do dependency injection, simply make the parameter the name of the global variable.
total = 0

def count(total):
  total += 1
  return total
print(count(total))


a = 10

# Parameters are local variables
def confusion(b):
  print(b)
  global a 
  a = 90

confusion(300)
# 1 - start with local
# 2 - check with parent
# 3 - check with global
# 4 - built in python functions