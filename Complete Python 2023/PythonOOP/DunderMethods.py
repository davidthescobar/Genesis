# Dunder methods allow modification

class Toy():
  def __init__(self, color, age):
    self.color = color
    self.age = age
    self.my_dict = {
      'Name': 'Yoyo',
      'Has Pets': False
    }

  def __str__(self):
    return f'{self.color}'

  def __len__(self):
    return 5

  def __call__(self):
    return 'yes?'

  def __getitem__(self, i):
    return self.my_dict[i]

action_figure = Toy('Blue', 0)


print(len(action_figure))
print(action_figure())
print(action_figure['Name'])

# These both print the same thing
print(action_figure.__str__())
print(str(action_figure))