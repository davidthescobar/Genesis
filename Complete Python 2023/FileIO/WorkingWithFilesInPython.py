# When a file is opened, the cursor goes to zero
my_file = open('app/test.txt')


# .seek() sets the cursor for open
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())

# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())

# Creates a list for each line
print(my_file.readlines())


my_file.close()