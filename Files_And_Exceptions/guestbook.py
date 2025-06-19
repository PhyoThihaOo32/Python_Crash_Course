from pathlib import Path


path = Path("Files_And_Exceptions/guest_book.txt")
guest_count = 0


def clear_guest_list():
    if path.exists():
        path.write_text("")
        print("All the guest nams have been deleted.")
    else:
        print("Guest book file doesn't exit.")


while True:

    user_name = input(
        "Enter your user name \n('q' to quit)\n('d' to clear the list): "
    ).strip()
    if user_name.lower() == "q":
        break
    elif user_name.lower() == "d":
        clear_guest_list()
        continue

    with path.open("a") as file:
        file.write(user_name + "\n")

    print(f"Added '{user_name} to the list")
    guest_count += 1


print(f"Guest names so far: with total guest_count: {guest_count}")
with path.open("r") as file:  # r meaning open the file in read mode.
    for line in file:
        print("- " + line.strip())
