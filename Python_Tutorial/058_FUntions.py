# Python Functions

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Creating a Function
# In Python, a function is defined using the def keyword:

def my_function():
  print("Hello from a function")

# Calling a Function
# To call a function, use the function name followed by parentheses:

my_function()
# Output:
# Hello from a function

# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. 
# You can add as many arguments as you want, just separate them with a comma.

# Example with one argument (fname):
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
# Output:
# Emil Refsnes
my_function("Tobias")
# Output:
# Tobias Refsnes
my_function("Linus")
# Output:
# Linus Refsnes

# Number of Arguments
# By default, a function must be called with the correct number of arguments. 
# Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
# Output:
# Emil Refsnes

# Arbitrary Arguments, *args
# If you do not know how many arguments will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
# Output:
# The youngest child is Linus

# Keyword Arguments
# You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# Output:
# The youngest child is Linus

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments will be passed into your function, add two asterisks: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
# Output:
# His last name is Refsnes

# Default Parameter Value
# If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
# Output:
# I am from Sweden
my_function("India")
# Output:
# I am from India
my_function()
# Output:
# I am from Norway
my_function("Brazil")
# Output:
# I am from Brazil

# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)
# Output:
# apple
# banana
# cherry

# Return Values
# To let a function return a value, use the return statement:

def my_function(x):
  return 5 * x

print(my_function(3))
# Output:
# 15
print(my_function(5))
# Output:
# 25
print(my_function(9))
# Output:
# 45

# The pass Statement
# Function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

def my_function():
  pass

# Positional-Only Arguments
# You can specify that a function can have ONLY positional arguments by adding , / after the arguments:

def my_function(x, /):
  print(x)

my_function(3)
# Output:
# 3

# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:

def my_function(*, x):
  print(x)

my_function(x = 3)
# Output:
# 3

# Combine Positional-Only and Keyword-Only
# You can combine the two argument types in the same function.

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
# Output:
# 26

# Recursion
# Python also accepts function recursion, which means a defined function can call itself.

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
# Output:
# 
# Recursion Example Results
tri_recursion(6)
# Output:
# 1
# 3
# 6
# 10
# 15
# 21
