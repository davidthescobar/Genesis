# Decorators add additional funcitonality to other functions and act like variables

def my_decorator(func):
  def wrap_func():
    print('******')
    func()
    print('******')
  return wrap_func

@my_decorator
def hello():
  print('hello')
@my_decorator
def bye():
  print('goodbye')

bye()


# this is how a decorate actually works:
# a = my_decorator(hello)
