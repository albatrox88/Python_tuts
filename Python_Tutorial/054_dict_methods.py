# clear(): Removes all the elements from the dictionary
my_dict = {'name': 'Alice', 'age': 30}
my_dict.clear()
print(my_dict)  # Output: {}

# copy(): Returns a copy of the dictionary
my_dict = {'name': 'Alice', 'age': 30}
copied_dict = my_dict.copy()
print(copied_dict)  # Output: {'name': 'Alice', 'age': 30}

# fromkeys(): Returns a dictionary with the specified keys and value
keys = ['name', 'age', 'city']
values = 'Unknown'
my_dict = dict.fromkeys(keys, values)
print(my_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

# get(): Returns the value of the specified key
my_dict = {'name': 'Alice', 'age': 30}
print(my_dict.get('name'))  # Output: Alice

# items(): Returns a list containing a tuple for each key-value pair
my_dict = {'name': 'Alice', 'age': 30}
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 30)])

# keys(): Returns a list containing the dictionary's keys
my_dict = {'name': 'Alice', 'age': 30}
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])

# pop(): Removes the element with the specified key
my_dict = {'name': 'Alice', 'age': 30}
my_dict.pop('age')
print(my_dict)  # Output: {'name': 'Alice'}

# popitem(): Removes the last inserted key-value pair
my_dict = {'name': 'Alice', 'age': 30}
my_dict.popitem()
print(my_dict)  # Output: {'name': 'Alice'}

# setdefault(): Returns the value of the specified key. If the key does not exist, insert the key with the specified value
my_dict = {'name': 'Alice', 'age': 30}
print(my_dict.setdefault('city', 'Unknown'))  # Output: Unknown
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'Unknown'}

# update(): Updates the dictionary with the specified key-value pairs
my_dict = {'name': 'Alice', 'age': 30}
my_dict.update({'city': 'New York', 'age': 35})
print(my_dict)  # Output: {'name': 'Alice', 'age': 35, 'city': 'New York'}

# values(): Returns a list of all the values in the dictionary
my_dict = {'name': 'Alice', 'age': 30}
print(my_dict.values())  # Output: dict_values(['Alice', 30])
