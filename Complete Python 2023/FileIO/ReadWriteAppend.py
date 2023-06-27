
# read = r (start of file), write = w (overwrites), append = a (end of file)
# read & write = r+ (adds to start of file)
# Opens and closes file
with open('test.txt', mode = 'a') as my_file:
	text = my_file.write('It\'s me!')
	print(text)