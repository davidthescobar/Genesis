# list, set, dictionary
# quick way to create these with comprehensions
# it is short-hand form


# For a list:
# my_list = [param for param iterable (optional: conditional)]

# For a set:
# my_list = {param for param iterable (optional: conditional)}

# For a dictrionary
# pass_dict = {
#   'a': 1,
#   'b': 2
# }

# my_dict_comprehension = {k:v**2 for k,v in pass_dict.items()}

# print (my_dict_comprehension)

my_list = [char for char in 'hello'] # These are comprehension
my_list2 = [num for num in range(0,100)]
my_list3 = [num*2 for num in range(0,100)]
my_list4 = [num**2 for num in range(0,100)
           if num % 2 == 0]


# # same as this:
# my_list = []

# for char in 'hello':
#   my_list.append(char)


print(my_list)
print(my_list4)