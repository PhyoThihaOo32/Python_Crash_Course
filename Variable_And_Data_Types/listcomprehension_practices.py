# what is list comprehension?
# it is a way to create lists in a clean, one-line syntax.

# syntax: new_list = [expression for item in iterable if condition]

# Example 1: Square numbers from 1 to 5.

squares = [ number ** 2 for number in range(1,11)]
print(squares)

# Example 2: Get even numbers from a list.

num = [1,2,3,4,5,6,7,8,9,10]
even = [ x for x in num if x % 2 == 0]
print(even)


odd = [x for x in num if x % 2 != 0]
print(odd)

# example 3: Convert words into uppercase

words = ['home','tittok','pharmacy','golf']
upper = [word.upper() for word in words]
print(upper)

# Example 4: remove vowel from string

str = 'Hello World'
vowel = 'aeiou'

no_vowel = [c for c in str if c not in vowel]
print(no_vowel)

# exercise: filter out words short than 5 letter

words = ['cat', 'elephant', 'sun', 'bicycle', 'tree', 'notebook', 'dog', 'universe', 'pen', 'laptop']
longer_words = [word for word in words if len(word) >= 5]
print(longer_words)

# exercise: flatten a 2D list

matirx = [[1,2],[3,4],[5,6]]
flat = [item for list in matirx for item in list]
print(flat)