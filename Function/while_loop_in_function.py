# countdown timer

def countdown():
    start_time = int(input('Set your time: '))
    while start_time > 0:
        print(f'{start_time} ')
        start_time -= 1
    print('Time up!')

countdown()

# number guessing game

def guess_number():
    secret_number = 7
    guess_number = None
    while guess_number != secret_number:
        guess_number = int(input('Guess the number 0-9: '))
        if guess_number < secret_number:
            print('Too Low.')
        else: 
            print('Too high')
        
    print('Correct! Secret number is 7')

guess_number()
    

# login system 

def user_login():
    correct_username = 'phyo'
    correct_password = 'phyo123'
    attempts = 3
    while attempts > 0:
        username_input = input('Enter username: ')
        userpassword_input = input('Enter userpassword: ')
        if username_input == correct_username and userpassword_input == correct_password:
            print('Login successful')
            return True
            
        else:
            attempts -= 1
            print(f'Please try again. You have {attempts} left')
    print('Account locked')
    return False


if user_login():
    print('Please enjoy our new website')
else:
    print('Please contact the customer support for password recovery')