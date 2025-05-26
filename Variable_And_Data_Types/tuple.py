# A tuple is a collection in Python that is:
# ordered / immutable / allows duplications

# creating a tuple

mytuple = (1,2,3)
empty_tuple = ()
single_item = (3,) # note the comma

# accsessing tuple item

print(mytuple[0])
for item in mytuple:
	print(item)


# tuple methods

print(mytuple.count(1)) # count the occurance
print(mytuple.index(3))

mytuple = (9,8,7,6)
print(mytuple)					
	