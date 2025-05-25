available_toppings = ['mushrooms', 'olives', 'green peppers',
                        'pepperoni', 'pineapple', 'extra cheese']

for index, available_topping in enumerate(available_toppings,start=1):
    print(f'{index}: {available_topping}')


customer_toppings = input('How would you like your topping? You can choose at least three toppings.').split(',')
customer_toppings = [topping.strip() for topping in customer_toppings]


for customer_topping in customer_toppings :
    if customer_topping in available_toppings:
        print(f"Adding {customer_topping}.")
    else:
        print(f"Sorry, we don't have {customer_topping}.")
        
print("\nFinished making your pizza!")