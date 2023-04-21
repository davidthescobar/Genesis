basket = ['a','b','c','d','e','d']
print(sorted(basket)) # <-- This function returns a value (copies the list), so it can be called inside the print function
print(basket)

basket.sort() # <-- This method does not return a value, so it must be called outside of the print function. It actually modifies the original list.
print(basket)

basket.reverse()
print(basket)