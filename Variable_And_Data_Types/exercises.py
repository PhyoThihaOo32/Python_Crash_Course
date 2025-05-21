#Exercise1: LowerCase and UpperCase
#Converting  'PyThon ProGRamMing" to lowercase and then uppercase:

text = 'PyThon ProGRamInG'

print(text.lower())
print(text.upper())

#Converting Into Title Style

print(text.title())

# Exercise2: Count and Find
# print("HelloWorld".count('l'))
# count() method - counts how many times a substring appears
# find() method - finds index of substring

print(text.lower().count('p'))
print(text)
print(text.find('a'))


# Exercise Replace and Strip
# Q: Romove spaces from " Python " and replace "y" with "i".

remove = " Python "
print(remove.strip())

replace = " Python "
print(replace.strip().replace('n','m'))


# Exercise Split and Join
# Q: Split "apple,banana,grape" and join with "|"

my_string = 'apple,banana,grape'
my_list = my_string.split(',')

print(my_list)

my_new_list = '|'.join(my_list)
print(my_new_list)   #apple|banana|grape

# Exercise: Check Type
# Q: Check f '12345' is all digit and 'Python3' is all letters.

number_only = '12345'
print(number_only.isdigit())

number_letter = 'Python3'
print(number_letter.isalnum())
print(number_letter.isalpha())
      
      
# Exercise: Start and End Check
#Q: Check if 'universe' starts with 'uni' and  end with 'verse'

my_string = 'universe'

print(my_string.startswith('uni'))
print(my_string.endswith('verse'))
