# Multiple inheritance is very powerful, but can get much more complex!


class User(object):
  def sign_in(self):
    print('Log in')


class Wizard(User):
  def __init__(self, name, power):
    self.name = name
    self.power = power

  def attack(self):
    print(f'Attacking with power of {self.power}')


class Archer(User):
  def __init__(self, name, num_arrows):
    self.name = name
    self.num_arrows = num_arrows
    
  def check_arrows(self):
    print(f'{self.num_arrows} arrows remaining')

  def run(self):
    print('run fast')


class HybridBorg(Wizard, Archer):
  def __init__(self, name, power, arrows):
    Archer.__init__(self, name, arrows) # Do this to solve multiple inheritance
    Wizard.__init__(self, name, power) # Do this to solve multiple inheritance


hb1 = HybridBorg('Borg', 50, 30)
print(hb1.sign_in())