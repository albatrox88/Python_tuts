# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# Example:
# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)  # Output: ['apple', 'banana', 'mango']

'''
list_name = [what to do for x in range(number) if condition]
'''




# With list comprehension you can do all that with only one line of code:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)  # Output: ['apple', 'banana', 'mango']



# The Syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.



# Condition
# The condition is like a filter that only accepts the items that evaluate to True.
# Example:
# Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]
print(newlist)  # Output: ['banana', 'cherry', 'kiwi', 'mango']



# The condition is optional and can be omitted:
# Example:
# With no if statement:
newlist = [x for x in fruits]
print(newlist)  # Output: ['apple', 'banana', 'cherry', 'kiwi', 'mango']



# Iterable
# The iterable can be any iterable object, like a list, tuple, set, etc.
# Example:
# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# Same example, but with a condition:
# Example:
# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)  # Output: [0, 1, 2, 3, 4]



# Expression
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
# Example:
# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
print(newlist)  # Output: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']



# You can set the outcome to whatever you like:
# Example:
# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)  # Output: ['hello', 'hello', 'hello', 'hello', 'hello']



# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
# Example:
# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)  # Output: ['apple', 'orange', 'cherry', 'kiwi', 'mango']

# The expression in the example above says:
# "Return the item if it is not banana, if it is banana return orange".
