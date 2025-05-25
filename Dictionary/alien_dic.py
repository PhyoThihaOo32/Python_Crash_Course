# A dictionary in python is a  collection of key_value pair.
# Each key is connected to value - which can be number, string, list or even dictionary - in fact any object.
# Key must be unique - if the duplicated key with override the old key
# Key can be any immutable type - string, tuple 

alien_dic = {
    'color': ['green', 'yellow', 'red'],
    'point': [2, 5, 10],
    'x_position': [0, 5, 10],
    'y_position': [5, 10, 15],
    'speed': ['slow','medium','fast']
}

red_alien = alien_dic['color'][1]
print(f' you shoot down the {red_alien} alien')
red_alien_point = alien_dic['point'][1]
print(f' you got {red_alien_point} points!')


# by using dict constructor 

fruits = dict(apple='red', banana="yellow", grape="purple")

fruit_list = [('apple', 'red'), ('banana', 'yellow'), ('grape', 'purple')]
fruits = dict(fruit_list)

print(fruits)

# inventory tracking example

inventory = {
    "banana": 40,
    "apple": 35,
    "mango": 20
}

inventory['apple'] -= 5
inventory['banana'] +=10
inventory.pop('mango')
inventory['lemon'] = 60

print(inventory)




