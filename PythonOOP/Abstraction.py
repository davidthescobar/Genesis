# Encapsulation is the binding of data and functions which manipulate that data. We encapsulate into one big object so everything is 
# Abstraction is the "hiding" of information, or giving acces to only what's neccesary.
class PlayerCharacter:
  membership = True
  def __init__(self, name, age):
      self.name = name
      self.age = age

  
  def run(self):
    return self.name # This is encapsulation, because an attribute from another method is used.

player1 = PlayerCharacter('Cindi', 19) # This is an instantiation


print(player1.run())