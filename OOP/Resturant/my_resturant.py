from icecream_stand import IceCreamStand as IC
from restaurant import Restaurant

my_icecream_stand = IC('Sweet Scoops', 'Ice Cream', 100, 'Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Mango')
my_icecream_stand.show_flavours()
my_icecream_stand.describe_restaurant()
my_icecream_stand.set_number_served(10)

my_resturant = Restaurant('Pizza Palace', 'Italian')
my_resturant.describe_restaurant()


