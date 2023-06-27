# Create a one-line lambda expession that squares the list.

my_list = [5,4,3]

print(list(map(lambda x: x**2, my_list)))


# sort a tuple list based on ascending from the second number

a = [(0,2), (4,3), (9,9), (10, -1)]

a_sort = sorted(a, key = lambda x: x[-1])

print(a_sort)