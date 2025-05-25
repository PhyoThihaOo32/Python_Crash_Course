# Simulating existing users in a real-world system
current_users = ['alice', 'bob', 'charlie', 'david', 'eve', 'frank']
new_users = ['grace', 'heidi', 'ivan', 'judy', 'mallory', 'bob', 'alice']

# Normalize current usernames to lowercase for comparison
normalized_current_users = [user.strip().lower() for user in current_users]

print("🔐 Checking new usernames...\n")

for new_user in new_users:
    normalized_user = new_user.strip().lower()
    
    if normalized_user in normalized_current_users:
        print(f"⚠️  Sorry, the username '{new_user.title()}' is already taken. Please choose a different one.")
    else:
        print(f"✅ The username '{new_user.title()}' is available.")