# A program that stores and recalls product locations

item_dict = {}
class Inventory():
	def update_location(self):
		while True:
			item_num = int(input('Enter item number '))
			item_aisle = int(input('Which aisle? '))
			item_bay = int(input('Which bay? '))
			aisle_bay_list = [item_aisle, item_bay]
			global item_dict
			item_dict.update({f'{item_num}': aisle_bay_list})
			y_n = str(input('Do you have another product (y/n)? '))
			if y_n == 'n':
				break

		# print(item_dict)


	def get_location(self):
		item = int(input('What is your item number? '))
		# print(item_dict[f'{item}'])
		aisle = item_dict[f'{item}']
		bay = item_dict[f'{item}']
		print(f'Item {item} is in aisle {aisle[0]} bay {bay[1]}')