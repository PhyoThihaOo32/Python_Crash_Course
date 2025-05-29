# creating empty dictionary

fav_places = {}

while True:

    # ask user for their name and their favourite places

    user_name = input("Hello Let us know who you are: 😎")
    user_fav_city = input("And Tell me your favourite city: 🚀")
    user_fav_place_in_city = input("What is your favourite place in the city! 😒 ")
    user_fav_food = input("Wait What is your favourite food in the city? 🤭")

    # adding user input into dictionary

    if user_name not in fav_places:
        fav_places[user_name] = {}
        fav_places[user_name]["city"] = user_fav_city
        fav_places[user_name]["place"] = user_fav_place_in_city
        fav_places[user_name]["food"] = user_fav_food

    user_option = input(
        "🤐To Quite the program 🫠 Press 1 and To would you like to add more person😍 Press 2"
    )

    if user_option == "1":
        print("OK i won't bother you anymore with my questions 😿")
        break
    elif user_option == "2":
        print("Great! Let give ask next person! 😏")
    else:
        print("Ohh no .. invalid input. Let me try again .. 😊")

print("Here is all about you and let tour all the city! 🤭")

for name, info in fav_places.items():
    print(f"Hello {name}. I Hope you enjoy the trip with us! ❤️")
    print(f"We will go your favourite place {info['place']} in {info['city']}🚕.")
    print(f"And we will go eat your favourite food {info['food']}🍼😁")
