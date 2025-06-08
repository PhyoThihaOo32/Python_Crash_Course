# argument is a value you pass to a functin when you call it. Python support several types of arguments.

# Positional Arguments: are passed in order. 

def greet(name, age, city='New York'):
    print(f"Hello my name is {name} and i am {age} year old")
    print(f"i am from {city}")

greet("Alice", 23)

# keyword arguements: specify which parameter each value goes to, using the  parameter name.

greet(age=22, name="Alice", city="Buffalo")

# Default Argument: you can assign the default value in the function definition

