# Write a program that ask the user how many people are in their dinner group.
# If the answer is more than eight, print a message saying they'll have to wait for a table.
# Otherwise, report that their table is ready.

user_number = int(input('How many people in your dinner group? '))

if user_number > 8:
    print("I'm sorry, but you'll need to wait for a table. Thank you for your patience.")
else:
    print("Excellent! Your table is ready! 🎉🍽️")