user_input = input('Type something (or type "exit" to quit): ')

if user_input == 'exit':
    print("Bye Bitch! 🫠")

else:
    print(f'That is what you said and what you will get: {user_input}.')


secret_number = '1'


while True:
    user_guess_number = input("Guess the secret number: (1-9) ")
    if user_guess_number != secret_number:
        print(f'Guess again! ')
    else:
        print(f'You got the number! 🍼')
        break