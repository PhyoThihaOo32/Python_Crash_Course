
def get_user_info():
    return {
        'name': 'Alice',
        'age': 24,
        'email': 'alice@email.com'
    }

user = get_user_info()

for key, value in user.items():
    print(f'{key}: {value}')

# returning dictionary with parameters

def get_name_in_dictionary(first_name, last_name, middle_name='', age= None):
    person_info = {
        'first_name': {first_name},
        'last_name': {last_name}
    }
    if middle_name:
        person_info [middle_name] = middle_name
    if age:
        person_info ['age'] = age

    return person_info

person_info = get_name_in_dictionary('Trump', 'Donald', age= 75)

print(person_info)


# use dict() constructor 

def student_score(name, score):
   return dict(name = name, score= score)

print(student_score('Jolie', 98))