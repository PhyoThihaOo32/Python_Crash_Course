responses = {}

# set the flag
is_true = True

while is_true:
    # get the user input 
    name = input('What is your name?  ')
    answer = input('Which mountain would you like to climb someday?  ')

    responses[name] = answer

    repeat = input('What you like to let another person respond? (yes/no)  ').lower()

    if repeat == 'no':
        print('Thank you! Enjoy the hike.')
        is_true = False


for name, answer in responses.items():
    print(f'{name} would like to climb {answer}')