# super refers to the class above

class User(object):
  def __init__(self, email):
    self.email = email
  def sign_in(self):
    print('Log in')

# This is a sub-class, or derived class.
class Wizard(User):
  def __init__(self, name, power, email):
    super().__init__(email) # This does the same thing as the comment below
    # User.__init__(self, email) # This calls the __init__ method of the parent class
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


w1 = Wizard('Merlin', 50, "merlin@outlook.com")
archer1 = Archer('Robbin', 30)

# Returns true because w1 is an instance of class Wizard
print(w1.email)