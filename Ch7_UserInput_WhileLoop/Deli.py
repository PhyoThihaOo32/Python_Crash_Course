ordered_sandwiches = [
    "turkey",
    "ham and cheese",
     "pastrami",
    "veggie",
    "chicken salad",
    "tuna",
     "pastrami",
    "BLT",
    "egg salad",
    "roast beef",
    "pastrami"
]

finished_sandwiches = []

print('Deli has run out of pastrami today')

while 'pastrami' in ordered_sandwiches:
    ordered_sandwiches.remove('pastrami')

while ordered_sandwiches:
    popped_sandwich = ordered_sandwiches.pop()
    finished_sandwiches.append(popped_sandwich)

print('Finished sandwiches for today:\n')

for index, finished_sandwich in enumerate(finished_sandwiches, start=1):
    print(f'{index}: {finished_sandwich}')

print('\nEvery sandwich made with love! 🥰❤️')




