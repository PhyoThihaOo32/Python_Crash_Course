# break : immediately exits the nearest loop (while or for), even if the loop condition is still True.

import random
random_numbers = [random.randint(0,10) for i in range(10)]

for i in random_numbers:
    if i == 5:
        print(f'Found your number: {i}')
        break
    print(f'Here we got number: {i}')


# continue : skips the rest of the current loop iteration and jumps to the next one

for num in range(10):
    if num == 5:
        continue
    print(num)

current_number = 0

for i in range(10):
    if i % 2 == 0:
        continue
    print(f'Here are the odd numbers: {i}')