# condtional tests

# tests for equality and inequality with strings

# user_input = input('Enter your password: ')

# password = '1234'

# if user_input == '1234':
#     print('Logged In')
# else:
#     print('Incorrect password')


# Conditional Tests

# Exercise 1: Grade Checker
student_score = int(input('Enter your score (0-100): '))

if 90 <= student_score <= 100:
    print('Grade: A')
elif 80 <= student_score <= 89:
    print('Grade: B')
elif 70 <= student_score <= 79:
    print('Grade: C')
elif 60 <= student_score <= 69:
    print('Grade: D')
elif 0 <= student_score < 60:
    print('Grade: F')
else:
    print('Invalid score 🫠')

# Exercise 2: Temperature Describer
temp = int(input('Enter the temperature in °F: '))

if temp > 90:
    print('It is very hot 🥵')
elif 70 <= temp <= 90:
    print("It's warm 😊")
elif 50 <= temp <= 69:
    print("It's mild 😌")
elif 30 <= temp <= 49:
    print("It's cold ❄️")
elif temp < 30:
    print("It's freezing 🥶")

# Exercise 3: Even or Odd Checker
number = int(input('Enter a number: '))

if number == 0:
    print('It is zero 💤')
elif number % 2 == 0:
    print('Even number ✌️')
else:
    print('Odd number 👆')


# stage of life 

age = int(input('Enter Age: '))

if age < 2:
    print('is a baby.')
elif 2 <= age < 4:
    print('is a toddler.')
elif 4 <= age < 13:
    print('is a kid.')
elif 13 <= age < 20:
    print('is a teenage.')
elif 20 <= age < 65:
    print('is an adult.')
elif age >= 65:
    print('is an elder')
else:
    print('Invalid')



