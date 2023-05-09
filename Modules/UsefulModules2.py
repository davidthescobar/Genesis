import datetime
# Array's are more performant than lists!
from array import array

print(datetime.time(4,23,2))
print(datetime.date.today())

# Lists in python are dynamic
# When using the array module, arrays are faster and take up less space
arr = array('i', [1,2,3])
print(arr[0])