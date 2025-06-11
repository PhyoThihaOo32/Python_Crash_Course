from users import User, Privillege


class Admin(User):

    def __init__(self, first_name: str, last_name: str, login_attempts: int = 0, **info):
         super().__init__(first_name, last_name, login_attempts, **info)
         self.privilleges = Privillege()
