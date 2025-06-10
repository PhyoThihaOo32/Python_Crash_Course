def make_profiles(first_name, last_name, **user_info):
    user_info['frst_name'] = first_name
    user_info['last_name'] = last_name
    for key, value in user_info.items():
        print(f'{key}: {value}')
    return user_info

make_profiles('Phyo', 'Oo', city="New York", age= 32)


# kwargs stands for keyword arguments. It let you pass any number of named arguments(key_value pairs)
# inside the function kwargs is a dictionary.


def greet_user(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

greet_user(name="Alice", age=25, city="New York")


# *args must come before **kwargs in a function definition.

