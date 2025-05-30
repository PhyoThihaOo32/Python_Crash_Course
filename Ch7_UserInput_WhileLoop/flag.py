flag = True

while flag:
    user_input = input("Type 'quit' to stop. ")
    if user_input == 'quit':
        flag = False
    else:
        print('You said: ',user_input)
print('Loop stopped')

# Flag to break on condition


import random

found = False
numbers = [random.randint(0,21) for i in range(20)]

print(numbers)

number = 0
while not found and number < len(numbers):
    if numbers[number] == 8:
        print(f'We found your number {numbers[number]}')
        found = True
    number += 1

if not found:
    print('8 is not in the list')
