#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('Tom', 1)
cat2 = Cat('Jeff', 2)
cat3 = Cat('Guss', 3)

# 2 Create a function that finds the oldest cat
def get_oldest_age(*args):
  return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {get_oldest_age(cat1.age,cat2.age,cat3.age)} years old')






# #Given the below class:
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # 1 Instantiate the Cat object with 3 cats
# cat1 = Cat('Tom', 1)
# cat2 = Cat('Jeff', 2)
# cat3 = Cat('Guss', 3)



# # 2 Create a function that finds the oldest cat
# def oldest_cat():
#   cats = {
#     'cat1': cat1.age,
#     'cat2': cat2.age,
#     'cat3': cat3.age
#   }
#   answer = max(cats.values())
#   return answer

# answer = oldest_cat()

# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# print(f'The oldested cat is {answer} years old.')