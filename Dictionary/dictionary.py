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
