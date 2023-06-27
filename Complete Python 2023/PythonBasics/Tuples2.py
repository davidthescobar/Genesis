# Tuple

my_tuple = (1,2,3,4,5)
new_tuple = my_tuple[1:2] # Tuples with only one item tend to leave a comma at the end
print(new_tuple)
x,y = my_tuple[0:2]
print(x)
print(y)
a,b,c,d, *other = (1,2,3,4,5)
print(other)

print(my_tuple.count(4))
print(my_tuple.index(4))
print(len(my_tuple))