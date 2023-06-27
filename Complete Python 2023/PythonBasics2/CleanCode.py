# Clean code

# Return evaluates to an expression, so we can use this instead of if/else
def is_even (num):
  return num % 2 == 0
print(is_even(51))

# We don't need an else statement
def is_even2 (num):
  if num % 2 == 0:
    return True
  return False
print(is_even2(51))

def is_even3 (num):
  if num % 2 == 0:
    return True
  else:
    return False
print(is_even3(51))



# % == modulo