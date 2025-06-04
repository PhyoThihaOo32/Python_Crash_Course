# Start with the users that need to be verified

unverified_users = ['alice', 'brian', 'candace', 'david', 'eve']
verified_users = []

# Verify each users from unverified_users lists

while unverified_users:
    verified_user = unverified_users.pop()
    print(f'Checking for user name with {verified_user} . . .')

# move each verifed users into list of verified_users
    verified_users.append(verified_user)
    print(f'User {verified_user} is verified and added.')

# printing all verified users.
print('List of all verified users:')
for index, verified_user in enumerate(verified_users, start=1):
    print(f'{index}: {verified_user}')


    