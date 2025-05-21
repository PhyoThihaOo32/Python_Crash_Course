# List is an ordered, mutable collection of items. 
# List can hold elements of any type: numbers, strings, boolean, even other lists.

fruit_list = ['apple', 'orange', 'banana', 'mango']

# common list operations

print(fruit_list[0]) # get the first element 
print(fruit_list[-1]) # get the last element

# modifying Elements

fruit_list[0] = 'strawberry'
print(fruit_list)

# Adding Element

fruit_list.append('pineapple')  # add to end
fruit_list.insert(0,'dragon fruit') # insert new element at index 1
print(fruit_list)

#Remove elements

fruit_list.remove('dragon fruit')  # remove by value
fruit_list.pop()  # remove last element
popped_fruit = fruit_list.pop(0) # remvoe by index
del fruit_list[0]  # delete by index
print(fruit_list)

# different between del and pop
# del : after deleting you can no longer access the value
# pop : can access and let you work with the item being popped out 

print(popped_fruit)


# list length
print(len(fruit_list))

city = ['new york','chicago', 'buffalo']
want_to_avoid = city.remove('chicago')

print(want_to_avoid)