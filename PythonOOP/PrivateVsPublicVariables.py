# Encapsulation is the binding of data and functions which manipulate that data. We encapsulate into one big object so everything is 
# Abstraction is the "hiding" of information, or giving acces to only what's neccesary.
# Public
# Private: use '_' to indicate the variable should be private. If you see and underscore, it means it should not be modified! This is standard convention because python has no true way to make items private unlike other languages.
class PlayerCharacter:
  membership = True
  def __init__(self, name, age):
      self._name = name
      self._age = age

  def run(self):
    print('run')

  
  def speak(self):
    print(f'My name is {self._name}, and I am {self._age} years old.')

player1 = PlayerCharacter('Cindi', 100)
player1.name = '!!!' # bad because these are intended to be private!
player1.speak = 'BOOOO'

print(player1.speak)