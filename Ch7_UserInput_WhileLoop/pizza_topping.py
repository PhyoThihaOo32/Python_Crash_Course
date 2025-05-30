# write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
# As they enter each topping, print a message saying you'll add that topping to their pizza.

# active = True

# while active:
#     user_input = input('What are your choice of toppings (enter \'quit\' to stop adding:) ')
#     if user_input == 'quit':
#         print('Bye')
#         active = False
#     print(f'I am adding {user_input} to the pizza')

# A movie theater charges different ticket prices depending on a person's age.
# If a person is under the age of 3, the ticket is free.
# If they are between 3 and 12, the ticket is $10, and if they are over age 12, the ticket is $15.
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

prompt = '''Welcome to the Movie Theater! 🎥
Please enter your age to check the ticket price.
(Type '0' to finish.)\n'''



while True:
    try:
        user_input = int(input(prompt))
    except ValueError:
        print('Please enter a valid number: 🤨')
        continue

    if user_input == 0:
        break

    if user_input < 3:
        print('🎉 No worries, you got a free pass!\n')
    elif 3 <= user_input <= 12:
        print('🎟️ Ticket price is $10.\n')
    else:
        print('🎟️ Ticket price is $15.\n')

print('🍿 Enjoy the show! Goodbye!')