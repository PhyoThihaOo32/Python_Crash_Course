# Set - is an unordered collection of unique elements
# - no duplicates
# - no guaranteed order
# - support fast membership checks


# creating set

my_set = {1,2,3,4,"phyo"}
empty_set = set()

print(my_set)
print(empty_set)

# Adding elements

empty_set.add('apple')
empty_set.add('starbuck')
empty_set.add('beef taco')
print(empty_set)


# removing elemetns

empty_set.remove('beef taco')  # raise error if not found 
empty_set.discard('beef tacos') # no error if not found 

print(empty_set)

# check membership

if 'apple' in empty_set:
    print('apple in set')

# looping through the set

for item in empty_set:
    print(item)

# set operation between two sets

a = {1,2,3}
b = {3,4,5}

# Union (Combine)
print (a | b)  # it remove the duplicate and combine the unique elements

# Intersection (Common)
print(a & b) # it give you the common elements between sets

# Difference (Items in a, not in b)
print(a - b)

# Symmetric difference (items in either, but not both)
print(a^b)