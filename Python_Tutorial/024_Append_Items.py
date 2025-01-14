# Append Items
# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)  # Output: ['apple', 'banana', 'cherry', 'orange']



# Insert Items
# To insert a list item at a specified index, use the insert() method.
# Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)  # Output: ['apple', 'orange', 'banana', 'cherry']



# Extend List
# To append elements from another list to the current list, use the extend() method.
# Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)  # Output: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']



# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
# Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)  # Output: ['apple', 'banana', 'cherry', 'kiwi', 'orange']