# OOP
# init is a special method. Called a constructer method.
# self is the default param when defining a method

class PlayerCharacter:
  def __init__(self, name, age):
    self.name = name # attributes.
    self.age = age
  def run(self):
    print('run')
    return 'Done'

player1 = PlayerCharacter('Cindi', 19)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1.name, player1.age, player1.run()) # this calls the .name method on line 7. 'Self' is what refers to anything to the left of the '.' in '.name'
print(player2.name, player2.age, player2.run(), player2.attack)