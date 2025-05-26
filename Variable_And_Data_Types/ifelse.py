cars = ['toyota', 'honda', 'ford', 'bmw', 'tesla']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

carName = [car.upper() if car == 'bmw' else car.title() for car in cars[:]] # list comprehension
print(carName)


pizza_topping = ['pepperoni', 'mushrooms', 'onions', 'sausage', 'bacon', 'extra cheese', 'black olives', 'green peppers', 'pineapple', 'spinach']

print("Available toppings:")
for idx, topping in enumerate(pizza_topping, 1):
    print(f"{idx}: {topping}")


customer_topping = input(
    '''
1: pepperoni 
2: mushrooms
3: onions
4: sausage
5: bacon
6: extra cheese
7: black olives
8: green peppers
9: pineapple
10: spinach

Enter your topping: ''')

if customer_topping in pizza_topping:
    print ("Added 😃")
else:
    print(f'We don\'t have {customer_topping}. Sorry 😭')


car = 'toyota'

print(f'Is car == "toyota"? I predict True')
print(car == 'toyota')

