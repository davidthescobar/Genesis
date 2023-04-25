# While (condition) do (something)
# Use "break" to stop the loop
# 'Else' only works if there is not a 'break'

i = 0
while i < 50:
  print(i)
  i += 1
  break
else:
  print('Done with all the work')