# Nesting - can store multiple dictionaries in a list, or a list of items * as values * in a dictionary - 
# even dictionary inside another dictionary.

# # A list of Dictionaries

# alien_0 = {
#     'color': 'green',
#     'point': 5,
#     'speed': 'slow'
# }

# alien_1 = {
#     'color': 'yellow',
#     'point': 10,
#     'speed': 'medium',
# }

# alien_2 = {
#     'color': 'red',
#     'point': 15,
#     'speed': 'fast'
# }

# all_aliens_list = [alien_0, alien_1, alien_2]

# for alien in all_aliens_list:
#     print(alien)

# creat a list of empty alien

aliens = []

# create 30 aliens

for _ in range(30):
    alien = {
        'color': 'green',
        'point': 5,
        'speed': 'slow'
    }
    aliens.append(alien)

#print all aliens

for alien in aliens:
    print(alien)

# counting total number of aliens
print(f'Total number of aliens: {len(aliens)}')

# the first 10 aliens are green - 11 to 20 aliens are yellow - 21 to 30 aliens are red

for alien in aliens[9:21]:
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'
for alien in aliens[19:]:
        alien['color'] = 'red'
        alien['point'] = 15
        alien['speed'] = 'fast'     

for index, alien in enumerate(aliens, start=1):
    print(f'{index} : {alien}')


# list inside dictionary

# Practice 1

student = {
      'name': 'Alice',
      'grades': [89,90,92],
      'hobbies': ['reading', 'cycling', 'hiking']
}

# printing all grades

for grade in student['grades']:
      print(grade)

# printing all hobbies

for hobby in student['hobbies']:
      print(hobby)


# Practice 2: Dictionary of Lists

menu = {
    'drinks': ['coffee', 'tea', 'juice', 'water'],
    'snacks': ['chips', 'cookies', 'sandwich', 'fruit'],
    'meals': ['pasta', 'burger', 'salad', 'pizza']
}

for catagory, item in menu.items():
      print(f'{catagory.title()}')
      for index, drink in enumerate(item, start=1):
            print(f'{index}: {drink}')