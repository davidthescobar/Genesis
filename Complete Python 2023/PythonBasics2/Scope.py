# Scope is the variables you have access to. The "variables" within your scope
# Python has "functional scope"
# Any variables outside of a function are global.
# Any variables inside a function are functional.


# Global scope means anything on this file can access this variable
global_scope = 100

def func():
  functional_scope = 100

print(global_scope)
# print(functional_scope) # This variable is outsite of the "scope"