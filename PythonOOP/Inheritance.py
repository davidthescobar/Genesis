# Encapsulation is the binding of data and functions which manipulate that data. We encapsulate into one big object so everything is 
# Abstraction is the "hiding" of information, or giving acces to only what's neccesary.
# Public
# Private: use '_' to indicate the variable should be private. If you see and underscore, it means it should not be modified! This is standard convention because python has no true way to make items private unlike other languages.
# Inheritance allows new objects to inherit the properties of existing objects.abs


# These are all classes, but aren't wizard's and archer's also users?
# The answer is yes! That is why we have inheritance.
# To inherit, pass the class name in the paramaters.

class User:
  def sign_in(self):
    print('Log in')


# This is a sub-class, or derived class.
class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'Attacking with power of {self.power}')

# This is a sub-class, or derived class.
class Archer(User):
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows

  def attack(self):
    print(f'Attacking with arrows: Arrows left {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robbin', 100)

print(wizard1.sign_in())

archer1.