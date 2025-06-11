from restaurant import Restaurant

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type, max_capacity=20, *flavours):
        super().__init__(restaurant_name, cuisine_type, max_capacity=20)
        self.flavours = flavours

    def show_flavours(self):
        for index, flavour in enumerate(self.flavours, start=1):
            print(f'{index}: {flavour}')