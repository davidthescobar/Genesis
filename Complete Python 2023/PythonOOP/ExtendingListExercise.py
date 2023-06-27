# Create a super list
# Use class SuperList()
# Be able to access through index
# Use a modified __len__ dunder method. It must return 1000 always.


class SuperList(list):

  def __len__(self):
    return 1000


super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])