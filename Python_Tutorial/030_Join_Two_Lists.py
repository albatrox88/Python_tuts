# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways is by using the + operator.


# Example:
# Join two lists:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)  # Output: ['a', 'b', 'c', 1, 2, 3]




# Another way to join two lists is by appending all the items from list2 into list1, one by one:
# Example:
# Append list2 into list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)

print(list1)  # Output: ['a', 'b', 'c', 1, 2, 3]



# Or you can use the extend() method, where the purpose is to add elements from one list to another list:
# Example:
# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)  # Output: ['a', 'b', 'c', 1, 2, 3]
