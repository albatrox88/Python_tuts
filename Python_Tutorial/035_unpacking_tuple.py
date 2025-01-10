# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# Example:
# Packing a tuple:
fruits = ("apple", "banana", "cherry")




# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
# Example:
# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)   # Output: apple
print(yellow)  # Output: banana
print(red)     # Output: cherry





# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
# Example:
# Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)   # Output: apple
print(yellow)  # Output: banana
print(red)     # Output: ['cherry', 'strawberry', 'raspberry']





# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
# Example:
# Add a list of values to the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)   # Output: apple
print(tropic)  # Output: ['mango', 'papaya', 'pineapple']
print(red)     # Output: cherry
