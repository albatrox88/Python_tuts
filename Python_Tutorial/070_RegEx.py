
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.
# Import the re module:
import re

# RegEx Functions
# The re module offers a set of functions that allow us to search a string for a match:
# - findall(): Returns a list containing all matches
# - search(): Returns a Match object if there is a match anywhere in the string
# - split(): Returns a list where the string has been split at each match
# - sub(): Replaces one or many matches with a string

# Metacharacters
# Metacharacters are characters with a special meaning in Regular Expressions.
# Examples include: [], \, ., ^, $, *, +, ?, {}, |, ()

# Special Sequences
# Special sequences are patterns preceded by a backslash (\) with special meanings.
# Examples include: \A, \b, \B, \d, \D, \s, \S, \w, \W, \Z

# Sets
# Sets in RegEx are specified within square brackets [] and define a group of characters to match.
# Examples include: [arn], [a-n], [^arn], [0-9], [a-zA-Z], [+]

# The findall() Function
# The findall() function returns a list containing all matches in a string.
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)  # Output: ['ai', 'ai']

# The search() Function
# The search() function searches for a match in a string and returns a Match object if found.
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())  # Output: The first white-space character is located in position: 3

# The split() Function
# The split() function splits a string into a list based on matches found using a RegEx pattern.
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)  # Output: ['The', 'rain', 'in', 'Spain']

# The sub() Function
# The sub() function replaces matches in a string with a specified replacement.
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)  # Output: The9rain9in9Spain

# Match Object
# A Match Object is returned by search() and contains information about the match.
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)  # Output: <re.Match object; span=(5, 7), match='ai'>


#These code examples demonstrate the usage of various RegEx functions in Python along with corresponding comment statements explaining each functionality.# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.
# Import the re module:
import re

# RegEx Functions
# The re module offers a set of functions that allow us to search a string for a match:
# - findall(): Returns a list containing all matches
# - search(): Returns a Match object if there is a match anywhere in the string
# - split(): Returns a list where the string has been split at each match
# - sub(): Replaces one or many matches with a string

# Metacharacters
# Metacharacters are characters with a special meaning in Regular Expressions.
# Examples include: [], \, ., ^, $, *, +, ?, {}, |, ()

# Special Sequences
# Special sequences are patterns preceded by a backslash (\) with special meanings.
# Examples include: \A, \b, \B, \d, \D, \s, \S, \w, \W, \Z

# Sets
# Sets in RegEx are specified within square brackets [] and define a group of characters to match.
# Examples include: [arn], [a-n], [^arn], [0-9], [a-zA-Z], [+]

# The findall() Function
# The findall() function returns a list containing all matches in a string.
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)  # Output: ['ai', 'ai']

# The search() Function
# The search() function searches for a match in a string and returns a Match object if found.
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())  # Output: The first white-space character is located in position: 3

# The split() Function
# The split() function splits a string into a list based on matches found using a RegEx pattern.
txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)  # Output: ['The', 'rain', 'in', 'Spain']

# The sub() Function
# The sub() function replaces matches in a string with a specified replacement.
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)  # Output: The9rain9in9Spain

# Match Object
# A Match Object is returned by search() and contains information about the match.
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)  # Output: <re.Match object; span=(5, 7), match='ai'>
