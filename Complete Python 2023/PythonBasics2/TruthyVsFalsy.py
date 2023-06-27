is_old = 'hello'
has_license = 5

print(bool(is_old))
print(bool(has_license))

print(bool(''))
print(bool(0))

if is_old and has_license:
  print('You are old enough to drive')
else:
  print('checkout')