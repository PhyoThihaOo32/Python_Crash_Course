# dictionary compresion - creating dictornary in one compact line

# syntax: {key: value for item in iterable}

# example 1: Square Dictionary
squares = {num: num ** 2 for num in range(1,10) if num % 2 == 0}
print(squares)

cubes = {cubes: cubes ** 3 for cubes in range(1,9)}
print(cubes)

# example 2: Convert List in name

names = ['Phyo','Bob','Johnson','Scarlet']
names_dict = {name: len(name) for name in names}
print(names_dict)

# example 3: Flip keys and values in dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}
flipped_dict = {value: key for key, value in original_dict.items()}

print(flipped_dict)

# student grade converter:

student_scores = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'Diana': 88
}

student_grade_dict = {
    name: 
        'A' if score >= 90 else
        'B' if score >= 80 else
        'C' if score >= 70 else
        'D' if score >= 60 else 
        'F'
    
    for name, score in student_scores.items()
}

print(student_grade_dict)

# TryItYourself 6-1 Persons

person_info_dict = {
    'first_name':'Gilbert',
    'last_name': 'Scott',
    'age': 62,
    'city': 'Los Angeles'
}

print(person_info_dict['first_name'])
print(person_info_dict.get('last_name', 'Not Avaliable'))
print(person_info_dict.get('age'))
print(person_info_dict.get('city'))

# TryItYourself 6-2 Favourite Numbers

favourite_numbers = {
    'Phyo': 7,
    'Bob': 3,
    'Johnson': 12,
    'Scarlet': 5,
    'Alice': 9
}

for name, number in favourite_numbers.items():
    print(f'{name} favourite number is {number}')

# TryItYourself 6-3 Glossary

import textwrap

programming_glossary = {
    'list': 'A collection of items in a particular order, defined using square brackets [].',
    'dictionary': 'A collection of key-value pairs, defined using curly braces {}.',
    'variable': 'A named storage for a value that can change during program execution.',
    'if': 'A conditional statement that executes a block of code if its condition is true.',
    'elif': 'A conditional statement that checks another condition if previous if/elif conditions were false.',
    'else': 'A conditional statement that executes a block of code if all previous conditions were false.',
    'loops': 'Structures that repeat a block of code multiple times, such as for and while loops.'
}

for glossary, meaning in sorted(programming_glossary.items(), reverse=True):
    wrapped_text = textwrap.fill(f'{glossary}:\n{meaning}\n', width=60)
    print(wrapped_text + '\n')

