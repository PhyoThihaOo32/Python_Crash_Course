message = "hello world"
print(message)

messages = "Hello World!!!"
print(messages)

message = "Hellllooo Worldddd !!!!!!"
print(message)

#variables are label that can assign to the values

#1.Strings
#String is a series of characters. Anything inside quotes is considered a string in Python.

my_string = "This is a string."
my_string1 = 'This is also a string.'

print('I told my friend,"I am learning Python."')
print("The language Python is named after 'Monty Python', not the snake.")
print("One of Python's strength is its diverse and supportive community.")


#Methods in String

name = 'Ada Lovelace'

print(name.title()) #capitalizes first letter of each word
print(name.upper())
print(name.lower())
print(name.strip()) #removes whitespace from both ends
print(name.replace('a','o')) #replaces substring
print(name.split(' ')) #split string into list
print(name.isdigit()) #check if all characters are digits
print(name.isalpha()) #check if all characters are letters
print('-'.join(name.split(' ')))


# White Space in Python
# white space include spaces tabs \t  Newlines \n

name = 'Alice '
print(name + ' in wonder land.')

print('To do list:\n\t1.Eat\n\t2.Sleep\n\t3.Repeat')

stripping_white_space = '   hello   '
print(stripping_white_space.rstrip())
print(stripping_white_space.lstrip())
print(stripping_white_space.strip())

#In Python, to remove a preflix from a string you can use 'removeprefix('string')' method
#What is prefix and surfix?
#Prefix is a part of string that appear at the beginning.
#Surfix is a part of string that appear at the end.

my_prefix = "https://google.com"
my_extension = "myBook.pdf"

print(my_prefix.removeprefix('https://'))
print(my_extension.removesuffix('.pdf'))


