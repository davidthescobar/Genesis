from inventory import Inventory

while True:
	inv = Inventory()
	determined = int(input('Enter 1 to check an item in. Enter 2 to lookup an item. '))
	
	if determined == 1:
		inv.update_location()
	elif determined == 2:
		inv.get_location()
	else:
		print('Please enter 1 or 2')