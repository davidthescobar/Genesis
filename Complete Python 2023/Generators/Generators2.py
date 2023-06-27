# A generator does not take memory space and can pause and resume functions when next() is called.
# Generators are iterable

def generator_function(num):
  for i in range(num):
    yield i*2 # yield pauses the function until told to move forward


g = generator_function(100)
next(g)
next(g)
print(next(g))
# for item in generator_function(100):
#   print(item)
  