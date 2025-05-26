# List of registered users (empty for now)
registered_users = ['admin', 'alice', 'bob', 'carol', 'dave']

if registered_users:
    user_name = input("Enter your user name: ").strip().lower()

    if user_name in [user.lower() for user in registered_users]:
        if user_name == 'admin':
            print(f"Hello {user_name.title()}, would you like to see a status report?")
        else:
            print(f"Hello {user_name.title()}, thank you for logging in again ➤")

        # A fun bonus joke
        print(f"\nWait, listen to my joke, {user_name.title()}.\nWhy do programmers prefer dark mode?\nBecause light attracts bugs! 🐛💡")
    else:
        print("Not Authorized!")
else:
    print("We need to find some users!")