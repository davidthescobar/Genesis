# Write a tool that
# Runs a command to open and read a file
# Translate it to japaenese
# Using pip3 install translate
from translate import Translator

try:
	with open('test', mode='r') as my_file:
		text = my_file.read()
		translator= Translator(to_lang="en")
		translation = translator.translate(text)
		print(translation)
except FileNotFoundError as e:
	print('File not found.')
	print(e)