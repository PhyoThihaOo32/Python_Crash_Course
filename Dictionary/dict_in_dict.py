
    # # dict in dict

# users = {
#     "alice": {"age": 25, "city": "New York"},
#     "martin": {"age": 24, "city": "Portland"},
#     "bob": {"age": 30, "city": "Chicago"},
#     "susan": {"age": 28, "city": "San Francisco"},
# }

# # Accessing specific value
# print(
#     f"Alice is {users['alice']['age']} years old student, living in {users['alice']['city']}."
# )

# # loop through nested dictionary

# for name, student_info in users.items():
#     print(f"Student name: {name.title()}")
#     for key, value in student_info.items():
#         print(f"{key}: {value}")


# # adding and updating an entry

# users["hay mar"] = {"age": 28, "city": "New York"}

# users["alice"]["city"] = "Boston"


real_id = {
    "Nolan Jones": {
        "first_name": "Nolan",
        "last_name": "Jones",
        "dob": "1998-05-07",
        "address": "123 Main St, Denver, CO",
        "height": "6ft 2in",
        "ID_number": "A123456789",
    },
    "Emily Clark": {
        "first_name": "Emily",
        "last_name": "Clark",
        "dob": "1992-11-15",
        "address": "456 Oak Ave, Seattle, WA",
        "height": "5ft 7in",
        "ID_number": "B987654321",
    },
    "Michael Lee": {
        "first_name": "Michael",
        "last_name": "Lee",
        "dob": "1985-03-22",
        "address": "789 Pine Rd, Austin, TX",
        "height": "5ft 10in",
        "ID_number": "C112233445",
    },
    "Sophia Patel": {
        "first_name": "Sophia",
        "last_name": "Patel",
        "dob": "2000-08-30",
        "address": "321 Maple St, Boston, MA",
        "height": "5ft 5in",
        "ID_number": "D556677889",
    },
}


for name, info in real_id.items():
    print(f"Name: {name.title()}")
    for key, value in info.items():
        print(f"{key.title()}: {value.title()}")


pet_0 = {"name": "milo", "type": "cat", "age": 4, "owner": "Mrs.Lee"}
pet_1 = {"name": "buddy", "type": "dog", "age": 2, "owner": "Mr.Smith"}
pet_2 = {"name": "tweety", "type": "bird", "age": 1, "owner": "Ms.Jones"}
pet_3 = {"name": "nemo", "type": "fish", "age": 1, "owner": "Tom"}
pet_4 = {"name": "bella", "type": "rabbit", "age": 3, "owner": "Anna"}

pets_list = [pet_0, pet_1, pet_2, pet_3, pet_4]

for pet in pets_list:
    print(pet)
    print()


cities = {
    'yangon': {
        'country': 'Myanmar',
        'population': 5160000,
        'fun-fact': 'Yangon is known for the Shwedagon Pagoda, a 99-meter tall stupa covered with gold leaf and precious stones.'
    },
    'new york':{
        'country': 'USA',
        'population': 8419000,
        'fun-fact': 'New York City is home to the iconic Statue of Liberty and is known as "The City That Never Sleeps."'
    },
    'tokyo':{
        'country': 'Japan',
        'population': 13960000,
        'fun-fact': 'Tokyo is the world’s most populous metropolitan area and is famous for its cherry blossoms and cutting-edge technology.'
    }
}

for city, info_information in cities.items():
    print(f'city: {city.title()} ')
    for info, information in info_information.items():
        print(f'{info}: {information}')