#A lambda function is a small anonymous function.

#A lambda function can take any number of arguments, but can only have one expression.

#Syntax
#lambda arguments : expression
#The expression is executed and the result is returned:




# Example 1: Adding 10 to a number

# Create a lambda function that adds 10 to its input
x = lambda a: a + 10
# Call the lambda function with the argument 5 and print the result
print(x(5))  # Output: 15

# Explanation:
# x = lambda a: a + 10:
# lambda a: a + 10 creates an anonymous function that takes one argument 'a' and returns 'a + 10'.
# 'x' is assigned this lambda function.
# print(x(5)):
# x(5) calls the lambda function with 5 as the argument, returning 5 + 10 = 15.
# The result 15 is printed.




# Example 2: Multiplying two numbers

# Create a lambda function that multiplies two inputs
x = lambda a, b: a * b
# Call the lambda function with arguments 5 and 6 and print the result
print(x(5, 6))  # Output: 30

# Explanation:
# x = lambda a, b: a * b:
# lambda a, b: a * b creates an anonymous function that takes two arguments 'a' and 'b', and returns their product 'a * b'.
# 'x' is assigned this lambda function.
# print(x(5, 6)):
# x(5, 6) calls the lambda function with 5 and 6 as arguments, returning 5 * 6 = 30.
# The result 30 is printed.





# Example 3: Summing three numbers

# Create a lambda function that sums three inputs
x = lambda a, b, c: a + b + c
# Call the lambda function with arguments 5, 6, and 2, and print the result
print(x(5, 6, 2))  # Output: 13

# Explanation:
# x = lambda a, b, c: a + b + c:
# lambda a, b, c: a + b + c creates an anonymous function that takes three arguments 'a', 'b', and 'c', and returns their sum 'a + b + c'.
# 'x' is assigned this lambda function.
# print(x(5, 6, 2)):
# x(5, 6, 2) calls the lambda function with 5, 6, and 2 as arguments, returning 5 + 6 + 2 = 13.
# The result 13 is printed.





# Example 4: Using lambda inside another function

# Define a function that returns a lambda function
def myfunc(n):
    return lambda a: a * n

# Create a doubler function using myfunc
mydoubler = myfunc(2)
# Call the doubler function with argument 11 and print the result
print(mydoubler(11))  # Output: 22

# Explanation:
# def myfunc(n): return lambda a: a * n:
# 'myfunc' is a function that takes one argument 'n'.
# Inside 'myfunc', a lambda function is created that takes one argument 'a' and returns 'a * n'.
# 'myfunc' returns this lambda function.
# mydoubler = myfunc(2):
# myfunc(2) calls 'myfunc' with 2 as the argument, returning a lambda function that multiplies its input by 2.
# 'mydoubler' is assigned this lambda function.
# print(mydoubler(11)):
# mydoubler(11) calls the lambda function with 11 as the argument, returning 11 * 2 = 22.
# The result 22 is printed.





# Example 5: Creating a tripler function

# Create a tripler function using myfunc
mytripler = myfunc(3)
# Call the tripler function with argument 11 and print the result
print(mytripler(11))  # Output: 33

# Explanation:
# mytripler = myfunc(3):
# myfunc(3) calls 'myfunc' with 3 as the argument, returning a lambda function that multiplies its input by 3.
# 'mytripler' is assigned this lambda function.
# print(mytripler(11)):
# mytripler(11) calls the lambda function with 11 as the argument, returning 11 * 3 = 33.
# The result 33 is printed.






# Example 6: Using both doubler and tripler functions

# Call both mydoubler and mytripler functions with argument 11 and print the results
print(mydoubler(11))  # Output: 22
print(mytripler(11))  # Output: 33

# Explanation:
# print(mydoubler(11)):
# Calls 'mydoubler' with 11 as the argument, returning 11 * 2 = 22.
# The result 22 is printed.
# print(mytripler(11)):
# Calls 'mytripler' with 11 as the argument, returning 11 * 3 = 33.
# The result 33 is printed.
