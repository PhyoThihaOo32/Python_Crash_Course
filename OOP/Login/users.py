class User:
    def __init__(self, first_name: str, last_name: str, login_attempts: int = 0, **info):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        self.info = info

    def describe_user(self):
        print(f'\nUser Name: {self.first_name.title()} {self.last_name.title()}')
        if self.info:
            for key, value in self.info.items():
                print(f'{key.capitalize()}: {value}')
        else:
            print("No additional user info provided.")

    def greet_user(self):
        print(f'\nHello {self.first_name.title()} {self.last_name.title()}.\nWelcome!')

    def update_user_info(self, **update_info):
        self.info.update(update_info)
        print("\nUser info updated:")
        for key, value in update_info.items():
            print(f'{key.capitalize()}: {value}')

    def login_attempt(self):
        self.login_attempts += 1
        print(f'Login attempt #{self.login_attempts}')

    def reset_login_attempt(self):
        if self.login_attempts > 0:
            print(f'Resetting login attempts from {self.login_attempts} to 0.')
        else:
            print('No login attempts to reset.')
        self.login_attempts = 0

class Privillege:

    def __init__(self):
        self.privilleges = []
        
    def set_privillages(self, *privilleges):
        self.privilleges = privilleges

    def show_privilleges(self):
        if self.privilleges:
            for privillege in self.privilleges:
                print(privillege)
        else:
            print('Set Privilleges first.')


  
<<<<<<< HEAD:OOP/users.py
admin1 = Admin('Micky', 'Mouse', password= 'babymilo@123')
admin1.privilleges.set_privillages('can_add_post', 'can_delete_post', 'can_ban_user', 'can_block_user')
admin1.describe_user()
admin1.privilleges.show_privilleges()
=======


>>>>>>> c43e0f2091f640c1fa4cf4a2cb7df8ea42e08665:OOP/Login/users.py
        