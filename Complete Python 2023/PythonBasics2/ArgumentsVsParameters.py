# DRY
# Parameters are used when the function is defined. They determine what arguments can be used.
def say_hello(name, emoji):
  print(f"Hello {name} {emoji}")

# Arguments are the values passed through a function
# Argumnents are used when the function is called, or "invoked."
say_hello('David', 'emoji')
say_hello('Hodge', 'emoji')
say_hello('Phillip', 'emoji')