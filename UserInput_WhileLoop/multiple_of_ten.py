# Ask the user for a number, and then report wether the number is multiple of 10 or not.

# user_input = int(input('Enter any number: '))

# if user_input == 0:
#     print('Quitting...')
# elif user_input % 10 == 0:
#     print(f'{user_input} is a multiple of 10.')
# elif user_input % 9 == 0:
#     print(f'{user_input} is a multiple of 9.')
# elif user_input % 8 == 0:
#     print(f'{user_input} is a multiple of 8.')
# elif user_input % 7 == 0:
#     print(f'{user_input} is a multiple of 7.')
# elif user_input % 6 == 0:
#     print(f'{user_input} is a multiple of 6.')
# elif user_input % 5 == 0:
#     print(f'{user_input} is a multiple of 5.')
# elif user_input % 4 == 0:
#     print(f'{user_input} is a multiple of 4.')
# elif user_input % 3 == 0:
#     print(f'{user_input} is a multiple of 3.And it is Odd number')
# elif user_input % 2 == 0:
#     print(f'{user_input} is a multiple of 2.And it is Even number')
# else:
#     print('Invalid input.')


try:
    user_input = int(input('Enter any number: (0 to quit): '))
    if user_input == 0:
        print('Over and Out!')
    else:
        # adding multiple into list based on user_number
        multiple = [i for i in range(2,11) if user_input % i == 0]

        if multiple:
# ','.join(map(str, multiple)) explanation:
#   - multiple: a list of numbers (e.g. [2, 3, 5])
#   - str: a function that converts each number to a string
#   - map(str, multiple): applies str() to each number → ['2', '3', '5']
#   - join(): joins the list of strings into one string with commas → "2,3,5"
            print(f'{user_input} is a multiple of: {', '.join(map(str,multiple))}')
        else:
            print(f'{user_input} is not multiple of any number between 2-10.')
except ValueError:
    print('Invalid user input! Expecting a number not a String.... ')

     
            