# F-String was introduced in Python 3.6 and is now the preferred way of formatting strings.
# Before Python 3.6, we had to use the format() method.

# F-Strings
# F-string allows you to format selected parts of a string.
# To specify a string as an f-string, simply put an f in front of the string literal.

# Example:
# Create an f-string:
txt = f"The price is 49 dollars"
print(txt)

# Placeholders and Modifiers
# To format values in an f-string, add placeholders {}, which can contain variables, operations, functions, and modifiers.

# Example:
# Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)

# A placeholder can include a modifier to format the value, like .2f for fixed point number with 2 decimals.
# Example:
# Display the price with 2 decimals:
txt = f"The price is {price:.2f} dollars"
print(txt)

# Perform Operations in F-Strings
# You can perform Python operations inside the placeholders.

# Example:
# Perform a math operation in the placeholder and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)

# Execute Functions in F-Strings
# You can execute functions inside the placeholder.

# Example:
# Use the string method upper() to convert a value into uppercase letters:
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

# More Modifiers
# There are several other modifiers that can be used to format values.
# Here is a list of all the formatting types.

# String format()
# Before Python 3.6, we used the format() method to format strings.
# The format() method can still be used, but f-strings are faster and the preferred way to format strings.

# Example:
# Add a placeholder where you want to display the price:
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

# Multiple Values
# You can use more values by adding them to the format() method.

# Example:
# Format the price to be displayed as a number with two decimals:
txt = "The price is {:.2f} dollars"

# Index Numbers
# You can use index numbers to ensure values are placed in the correct placeholders.

# Example:
# Use index numbers to refer to values in the format() method:
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Named Indexes
# You can also use named indexes in format() by entering a name inside the curly brackets {carname}.

# Example:
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))
