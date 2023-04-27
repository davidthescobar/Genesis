# A function should do ONE thing very well, and should have a return.
# A return keyword exits the function

# This will return None
def sum(num1, num2):
  num1 + num2

print(sum(4, 5))


# This will return num1 + num2
def sum(num1, num2):
  def something(num1, num2):
    return num1 + num2
  return something

print(sum(5, 5))

total = sum(5,5)
print(sum(5, total))