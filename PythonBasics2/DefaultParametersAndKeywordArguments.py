# DRY
# Positional parameters
# Default Parameters
def say_hello(name='Darth Vader', emoji='Emoji'):
  print(f"Hello {name} {emoji}")

# Positional arguments
say_hello('David', 'emoji')
say_hello('Hodge', 'emoji')
say_hello('Phillip', 'emoji')


# Keyword arguments allow us to not worry about the position
say_hello(name='Bob', emoji='emoji')
# Here the default parameters are used
say_hello()