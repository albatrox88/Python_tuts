#Python - Tuple Methods
#Tuple Methods
#Python has two built-in methods that you can use on tuples.

# count(): Returns the number of times a specified value occurs in a tuple
my_tuple = (1, 2, 3, 2, 4, 2, 5)
count_2 = my_tuple.count(2)
print(count_2)  # Output: 3 (2 occurs 3 times in the tuple)

# index(): Searches the tuple for a specified value and returns the position of where it was found
index_4 = my_tuple.index(4)
print(index_4)  # Output: 4 (index of value 4 in the tuple)
