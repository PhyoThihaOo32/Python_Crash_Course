my_dictionary = {
    "name": "David",
    "age": 34
}

my_nested_dic = {
    "Sajjad": {"math": 100, "English": 78},
    "David": {"math": 89, "English": 98}

}

print(my_nested_dic["David"]["math"])

my_nested_dic["David"]["math"] = 100



my_nested_dic["Alex"] = {"math": 76, "English": 88}

print(my_nested_dic)


# print(my_nested_dic.keys())
# print(my_nested_dic.values())
# print(my_nested_dic.items())

#my_nested_dic.clear()

print(f'Getting David Info: {my_nested_dic.get("David")}') # get method

poped_out = my_nested_dic.pop("Sajjad")

print(poped_out)

