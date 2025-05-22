import random

#For Loops - loop through a sequence  [ list,string,range,etc]
#While Loops - loop while condition is true

#For Loop

fruits = ['mangon','coconut','grape','kiwi']
item_count = 1

for fruit in fruits:
  print(f'Item: {item_count} - {fruit}')
  item_count += 1

for i in range(5):
  print(i)

my_pizzas = ['pepperoni', 'margherita', 'hawaiian']

for pizza in my_pizzas:
  print(f'I like pizza: {pizza}')

print("New York city has the best Pizzas!")


my_animals = ['cats','dogs', 'birds']

for animal in my_animals:
  print(f'{animal} would make a great pet!')

print(f'Actually I love them all!')


#adding squares of numbers into list

squares = []

for i in range(1,11):
  
  squares.append(i**2)

print(squares)

#simple statstic with list of number

num_list = [random.randint(1,100) for _ in range(10)] # list comprehension
print(num_list)

print(max(num_list))
print(min(num_list))
print(sum(num_list))

cubes = [ _ ** 3 for _ in range(1,11)]
print(cubes)

