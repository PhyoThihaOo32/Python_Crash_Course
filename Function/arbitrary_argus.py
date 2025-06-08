def add_toppings(*user_toppings):
    for topping in user_toppings:
        print(f'-{topping}')



add_toppings('pepperoni', 'mushrooms', 'onions', 'green peppers')