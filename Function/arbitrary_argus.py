def add_toppings(size_of_pizza ='M', *user_toppings):
    print(f'Size: {size_of_pizza}')
    for topping in user_toppings:
        print(f'-{topping}')



add_toppings('L',*['pepperoni', 'mushrooms', 'onions', 'green peppers'])