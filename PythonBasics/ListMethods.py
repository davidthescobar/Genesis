basket = [1,2,3,4,5]
print(len(basket))


# adding
# new_list = basket.append(100) # appends a value in place. Does not copy!
# print(new_list)
# basket.append(100)
# new_list = basket
# print(new_list)

# basket.insert(1,100)
# new_list = basket
# print(new_list)

new_list = basket.extend([100,101])
# print(basket)
print(new_list)

# removing
basket.pop() # give the index
basket.pop(1)
basket.remove(5) #give the value
basket.clear()
print(basket)

basket.extend