# List Slicing
# Lists ARE mutable
amazon_cart = [
  'notebooks', 
  'sunglasses', 
  'toys', 
  'grapes'
]
amazon_cart[0] = 'laptop' # This is not slicing
print(amazon_cart[0:3]) # List slicing creates a new copy of the list
print(amazon_cart)
