
def highest_even (li):
  '''
  Returns the maximum even number in a given list
  '''
  answer = []
  for item in li:
    if item % 2 == 0:
      answer.append(item)
  print(max(answer))
highest_even([5,10,12,5,4,6,8,11])