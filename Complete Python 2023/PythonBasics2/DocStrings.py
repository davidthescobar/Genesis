#Docstrings allow comments inside of a function to provide documentation for an IDE

def test (a):
  '''
  Info: This function tests a prints param a
  '''
  print(a)

test('!!!')
help(test)

# Magic Method (Dunder Method)
print(test.__doc__)