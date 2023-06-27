# Encapsulation is the binding of data and functions which manipulate that data. We encapsulate into one big object so everything is 
class PlayerCharacter:
  membership = True
  def __init__(self, name, age):
      self.name = name
      self.age = age

  
  def run(self):
    return self

player1 = PlayerCharacter('Cindi', 19) # This is an instantiation


print(player1.run())