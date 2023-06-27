# OOP
# init is a special method. Called a constructer method.
# self is the default param when defining a method. It referes to the Class

# Class
class PlayerCharacter:
  # Class Object Attribute -> Static. Kind of like a global attribute for 
  # everything in the class.
  membership = True
  # Method
  # This __init__ method is called everytime we instantiate
  def __init__(self, name='anonymous', age=0):
    if (age > 18): # (or self.membership)
      self.name = name # attributes. -> Dynamic
      self.age = age
  # def __init__(self, name, age):
  #   if (PlayerCharacter.membership): # (or self.membership)
  #     self.name = name # attributes. -> Dynamic
  #     self.age = age

  
  def shout(self):
    print(f'my name is {self.name}')
    return 'Done'

  def run(self, speed):
    print(f'my name is {self.name}')
    return 'Done'

player1 = PlayerCharacter('Cindi', 19) # This is an instantiation
player2 = PlayerCharacter('Tom', 21) # This is an instantiation
player2.attack = 50

print(player1.name, player1.age, player1.shout(), player1.run('fast')) # this calls the .name method on line 7. 'Self' is what refers to anything to the left of the '.' in '.name'
print(player2.name, player2.age, player2.shout(), player2.run('slow'), player2.attack)