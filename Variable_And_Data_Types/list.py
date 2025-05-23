# organizing the list

list = ['toyota','kia','bmw','acura']

# sorting permanently with sort method

list.sort()
print(list)
list.sort(reverse=True)
print(list)

# sorting temporatily with the sorted Function

print("this is original list: ", list)
print("this is sorted list: ", sorted(list))
print("this is also the sorted list in reversed: ", sorted(list, reverse=True))


# printing list in reverse order
# reverse method also change the order permanently

city = ['new york','yangon','mandalay', 'tokyo']

city.reverse()
print(city)

# find the length of the list by using len function
# python counts the items in a list startig with one

print(len(list))