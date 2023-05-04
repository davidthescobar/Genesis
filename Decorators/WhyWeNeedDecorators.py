#Decorator

#Create our own decorator that tests the performance of our code
from time import time
def performance(fn):
  def wrapper(*args, **kwargs):
    t1 = time()
    result = fn(*args, **kwargs)
    t2 = time()
    print(f'took {t2-t1}ms')
    return result
  return wrapper


@performance
def long_time():
  for i in range(1000):
    i*5

long_time()