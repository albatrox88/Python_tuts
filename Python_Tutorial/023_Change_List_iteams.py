# Change a Specific Item
# To change a specific item in the list, refer to its index and assign a new value:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)  # Output: ['apple', 'blackcurrant', 'cherry']



# Change a Range of Item Values
# To change a range of items, define a new list with the replacement values and refer to the range of index numbers:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)  # Output: ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']



# If you insert more items than you replace, the new items will be inserted, and the remaining items will shift:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)  # Output: ['apple', 'blackcurrant', 'watermelon', 'cherry']



# If you insert fewer items than you replace, the list will shorten:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)  # Output: ['apple', 'watermelon']



# Insert Items
# To insert a new item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon") #(index,value)
print(thislist)  # Output: ['apple', 'banana', 'watermelon', 'cherry']
