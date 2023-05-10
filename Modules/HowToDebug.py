# debugging

# Use linting - software detection of problems in code
# Use an IDE or editor - they have many tools for debugging specifically
# Learn to read errors
# Use the pdb module (python debugger)


# 'step' 'a' 'help' 'exit'
import pdb

def add(num1, num2):
  pdb.set_trace() # Use 'step' in the temrinal to move to the next line
  t = 4*5
  return num1 + num2

add(4, 'lol')