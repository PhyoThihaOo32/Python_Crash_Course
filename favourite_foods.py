# favorite fruite program

favourite_fruit = input('Enter your three favourite fruit(seperated by comma): ').split(',')
favourite_fruit = [fruit.strip() for fruit in favourite_fruit]

my_favourite_fruit = ['apple', 'banana', 'mango', 'orange', 'grape']

for fruit in favourite_fruit:
    if fruit in my_favourite_fruit:
        print(f'We both like {fruit}')
    else:
        print(f'I should try {fruit} too.')