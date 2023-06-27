picture = [
[0,0,0,1,0,0,0],
[0,0,1,1,1,0,0],
[0,1,1,1,1,1,0],
[1,1,1,1,1,1,1],
[0,0,0,1,0,0,0],
[0,0,0,1,0,0,0]
]


for row in picture:
  for pixel in row:
    if pixel:
      print('*', end = '')
    else:
      print(' ', end = '')
  print('') # Creates new line after every row




# for i in picture:
#   image = ''
#   for x in i:
#     if x == 0:
#       image = image + ' '
#     else:
#       image = image + '*'
#   print (image)

# for image in picture:
#   for pixel in image:
#     if (pixel):
#       print('*', end ="")
#     else:
#       print(' ', end ="")
#   print('')