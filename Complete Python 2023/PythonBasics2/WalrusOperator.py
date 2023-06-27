# Walrus Operator: :=
# Assigns values to variabls as part of a larger expression

a = 'hello'

if (n := len(a)) > 4:
  print(f'Too long {n} elements.')

while ((n := len(a)) > 1):
  print(n)
  a = a[:-1]

print(a)