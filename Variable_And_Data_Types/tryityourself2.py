#Personnal Message

name = 'Eric'
welcome_message = f'Hello {name}, would you like to learn some Python today?'
print(welcome_message)

#Name Case

print(name.lower())
print(name.upper())
print('Alice in the wonderland'.title())

#Famous Quotes

famous_quote = '"Programming isn\'t about what you know; it\'s about what you can figure out."'
famous_person_name = 'Chirs Pine'

print(f'{famous_quote} _said by {famous_person_name}.')

#removing prefix and suffix

file_extension = 'index.html'
prefix_link = 'https://www.google.com'

print(file_extension.removesuffix('.html'))
print(prefix_link.removeprefix('https://'))