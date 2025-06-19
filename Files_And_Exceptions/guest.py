from pathlib import Path

# prompt user for their name
user_name = input("Please enter your name: ").strip()

path = Path("Files_And_Exceptions/username.txt")

# Create directory if needed
path.parent.mkdir(parents=True, exist_ok=True)

# Append the name to the file (add a new line)
with path.open("a") as file:
    file.write(user_name + "\n")

print(f"Added '{user_name}' to the list.")
