# Seeing the world

# storing location unalphabetically in a list

locations = ['Tokyo','Alaska','Oregon','Hawaii','Bagan']

# printing list in raw

print(locations)

# sorting list in alphabectical order

sorted_locations = sorted(locations)

# printing list in original order
print(sorted_locations)

# using sorted to print list in reverse-alphabetical order

print(sorted(sorted_locations, reverse=True))

# showing original list
print(locations)

# reverse the list - permanently

locations.reverse()  # return none
print(locations)

# reverse back to original

locations.reverse()
print(locations)

# sorting list permenantly in alphabetical order

locations.sort()
print(locations)

# printing reversed-aphabetical order

locations.sort(reverse=True)
print(locations)

# print number of the city(locations)

number_locations = len(locations)
print(f"Total locations: {number_locations}")


