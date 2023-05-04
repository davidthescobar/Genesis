# Errors that crarsh our program are called 'exceptions'
# Anything inside the try block, if error run the except block

# best practice is to always use the actual exception for readability

def sum(num1, num2):
  try:
    return num1/num2
  except (TypeError, ZeroDivisionError) as err:
    print({err})

print(sum('1',2))