# Slicing is a way to extrect a portion of a list using a special syntax:
# list [start(inclusive):stop(off-by-one/exclusive):step]

num = [0,1,2,3,4,5,6,7,8,9]

# slice from index 2 to 5
print(num[2:5]) # 2,3,4

# slice from start to index n 

print(num[:4]) # 0 1 2 3

# slice from index n to end

print(num[5:]) # 5 6 7 8 9

# slice with step of 2 

print(num[::2])

# reverse the list

print(num[::-1])

# slicing negative index

print(num[-3:]) # print last 3 item
print(num[:-3]) # ommiting last three item

# looping through a slice

cities = ["New York", "London", "Tokyo", "Paris", "Sydney", "Berlin", "Toronto", "Dubai", "Singapore", "Barcelona"]


slice_city = [city for city in cities[3:11] if city.startswith(('N','P','L'))]
print(slice_city)

