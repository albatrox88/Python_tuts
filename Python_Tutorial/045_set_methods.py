#Set Methods
#Python has a set of built-in methods that you can use on sets.
# add(): Adds an element to the set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'cherry', 'orange'}

# clear(): Removes all the elements from the set.
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)  # Output: set()

# copy(): Returns a copy of the set.
fruits = {"apple", "banana", "cherry"}
fruits_copy = fruits.copy()
print(fruits_copy)  # Output: {'apple', 'banana', 'cherry'}

# difference(): Returns a set containing the difference between two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
diff = set1.difference(set2)
print(diff)  # Output: {1, 2}

# difference_update(): Removes the items in this set that are also included in another specified set.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.difference_update(set2)
print(set1)  # Output: {1, 2}

# discard(): Remove the specified item from the set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)  # Output: {'apple', 'cherry'}

# intersection(): Returns a set that is the intersection of two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersect = set1.intersection(set2)
print(intersect)  # Output: {3}

# intersection_update(): Removes the items in this set that are not present in other specified sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.intersection_update(set2)
print(set1)  # Output: {3}

# isdisjoint(): Returns whether two sets have an intersection or not.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # Output: True (No common elements)

# issubset(): Returns whether another set contains this set or not.
set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # Output: True (set1 is a subset of set2)

# issuperset(): Returns whether this set contains another set or not.
set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))  # Output: True (set1 contains set2)

# pop(): Removes and returns an arbitrary element from the set.
fruits = {"apple", "banana", "cherry"}
removed_fruit = fruits.pop()
print(removed_fruit)  # Output: 'apple'
print(fruits)  # Output: {'banana', 'cherry'}

# remove(): Removes the specified element from the set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'cherry'}

# symmetric_difference(): Returns a set with the symmetric differences of two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)  # Output: {1, 2, 4, 5}

# symmetric_difference_update(): Inserts the symmetric differences from this set and another.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 2, 4, 5}

# union(): Returns a set containing the union of sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# update(): Updates the set with the union of this set and others.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)  # Output: {1, 2, 3, 4, 5}
