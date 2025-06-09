class User:
    def __init__(self, first_name, last_name, **info):
        self.first_name = first_name
        self.last_name = last_name
        self.info = info
        
    def describe_user(self):
        print(f'User name: {self.first_name} {self.last_name}')
        for key, value in self.info.items():
            print(f'{key}: {value}')

    def greet_user(self):
        print(f'Hello {self.first_name} {self.last_name}.\nWelcome!')

    def update_user_info(self, **update_info):
        self.info.update(update_info)

first_user = User('Phyo','Oo', age=24, city='New York')

first_user.describe_user()
first_user.greet_user()
first_user.update_user_info(ethnicity='Burmese')
first_user.describe_user()