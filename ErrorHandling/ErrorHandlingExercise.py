# Errors that crarsh our program are called 'exceptions'
# Anything inside the try block, if error run the except block

# best practice is to always use the actual exception for readability

while True:
  try:
    age = int(input('What is your age? '))
    10/age # This will ValueError
  except ValueError:
    print('Please enter a number')
  except ZeroDivisionError:
    print('Please enter a number')
  else:
    print('Thank you!')
    break
  finally:
    print('Finished')