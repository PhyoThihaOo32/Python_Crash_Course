class Restaurant:
    def  __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type

    def describe_resturant(self):
        print(f'Name of resturant: {self.resturant_name}')
        print(f'Cuisine type: {self.cuisine_type}')

    def open_resturant(self):
        print(f'{self.resturant_name} is now open!')

my_resturant = Restaurant('Mandalay', 'Burmese Foods')

print(my_resturant.resturant_name)
print(my_resturant.cuisine_type)

my_resturant.describe_resturant()
my_resturant.open_resturant()