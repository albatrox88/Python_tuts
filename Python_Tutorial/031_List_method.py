#List Methods
#Python has a set of built-in methods that you can use on lists.
# append(): Adds an element at the end of the list
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# clear(): Removes all the elements from the list
fruits.clear()
print(fruits)  # Output: []

# copy(): Returns a copy of the list
fruits = ['apple', 'banana', 'cherry']
fruits_copy = fruits.copy()
print(fruits_copy)  # Output: ['apple', 'banana', 'cherry']

# count(): Returns the number of elements with the specified value
fruits = ['apple', 'banana', 'cherry', 'banana']
count_banana = fruits.count('banana')
print(count_banana)  # Output: 2

# extend(): Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana']
more_fruits = ['cherry', 'orange']
fruits.extend(more_fruits)
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# index(): Returns the index of the first element with the specified value
fruits = ['apple', 'banana', 'cherry']
index_cherry = fruits.index('cherry')
print(index_cherry)  # Output: 2

# insert(): Adds an element at the specified position
fruits.insert(1, 'orange')
print(fruits)  # Output: ['apple', 'orange', 'banana', 'cherry']

# pop(): Removes the element at the specified position
fruits.pop(2)
print(fruits)  # Output: ['apple', 'orange', 'cherry']

# remove(): Removes the item with the specified value
fruits.remove('orange')
print(fruits)  # Output: ['apple', 'cherry']

# reverse(): Reverses the order of the list
fruits.reverse()
print(fruits)  # Output: ['cherry', 'apple']

# sort(): Sorts the list
numbers = [3, 1, 2]
numbers.sort()
print(numbers)  # Output: [1, 2, 3]
