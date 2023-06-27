
# '/' allows us to specify a directory as a RELATIVE PATH
# ./ would mean current folder
# ../ would mean back a folder
with open('app/test.txt', mode = 'r') as my_file:
	print(my_file.read())