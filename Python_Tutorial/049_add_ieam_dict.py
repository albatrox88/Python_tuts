# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it.

# Example
# Add a new item "color" to the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# Update Dictionary
# The update() method will update the dictionary with the items from a given argument.
# If the item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.

# Example
# Add a "color" item to the dictionary by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
