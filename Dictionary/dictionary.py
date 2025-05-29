# What is dictionary?
# A dictionary stores data as key-value pairs, like a real dictionary.

# Syntax:

user = {
    "name" : "Alice",
    "age" : 25,
    "city" : "New York"
}

# Accessing Values:

print(user["name"])
print(user["age"])
print(user["city"])

# using get method to access the values
print(f'Using get method to get the name {user.get('name')}')
print(user.get('address','Address is not avaliable'))

# Adding/Updating: 

user["email"] = "alice25@gmail.com"
user["age"] = 28
user.update({"age": 18})


# Looping through Dictionary:

for key, value in user.items():
    print(f'{key.title()}: {value}')

# removing items:

del user['city']
removed_age = user.pop('age')
print(removed_age)

# Username Database:

users = {
    'alice': {'age': 28, 'email': 'alice34@gmail.com'},
    'peter': {'age': 30, 'email': 'peterpen@gmail.com'}
}

print(users['alice']['email'])


# TryItYourself Rivers:

river_dict = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    'mississippi': 'united states',
    'ganges': 'india',
    'thames': 'united kingdom',
    'seine': 'france',
    'colorado': 'united states'
}

for river, country in river_dict.items():
    print(f'{river.title()} runs through {country.title()}')

print('List of rivers in my dictionary: ')
for index, river in enumerate(river_dict.keys(),start=1):
    print(f'{index}: {river}')

print('List of country in my dictionary: ')
for index, country in enumerate(sorted(set(river_dict.values()))):
    print(f'{index}: {country.title()}')
                                