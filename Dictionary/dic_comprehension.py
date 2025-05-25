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