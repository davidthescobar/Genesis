# While loops are more flexible/more powerful. Must create a stopping point.
# For loops are simpler
# When to use a while vs for loop

# Using while loops when you're not sure how long the loop should take.
# Use for loops when you know how long the loop needs to take.


while True:
  response = input('Say someting: ')
  if (response == 'bye'):
    break


my_list = [1,2,3]
for i in my_list:
  print(i)

i = 0
while i < len(my_list):
  print(my_list[i])
  i += 1