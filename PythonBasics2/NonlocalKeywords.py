# Nonlocal keyowrd is used for variables that are not global, but outside the scope of a function

# Scope - what variables do I have access to?

def outer():
  x = 'local'
  def inner():
    nonlocal x
    x = 'nonlocal'
    print('inner', x)
  inner()
  print('outer', x)

outer()

x = 'Hello'[0]


print(x)

# 1 - start with local
# 2 - check with parent
# 3 - check with global
# 4 - built in python functions