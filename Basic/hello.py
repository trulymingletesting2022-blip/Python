#  This is a simple Python program that prints "Hello, World!".
# print("Hello, World!")

#  Indentation in Python
# In Python, Indentation is used to define blocks of code. It indicates to the Python interpreter that a group of statements belongs to the same block. All statements with the same level of indentation are treated as part of the same code block. Indentation is created using whitespace at the beginning of each line, and the commonly accepted convention is to use four spaces per indentation level.
# Example of indentation in Python:
# print("I have no Indentation ")
#     print("I have tab Indentation ")
    
# In the above example, the first print statement is not indented, while the second print statement is indented with a tab. This will result in an IndentationError when you run the code, because Python expects consistent indentation levels. To fix this, you should ensure that both print statements have the same level of indentation, either by using spaces or tabs consistently throughout your code.

# Input and Output in Python
# Taking Input using input()
# name = input("Enter your name:")
# Printing Output using print()
# print("Hello, " + name + "! Welcome to python programming.")

# Taking multiple input in python
# We are taking multiple input from the user in a single line, splitting the values entered by the user into separate variables for each value using the split() method.
# x,y,z = input("Enter two values:").split()
# print("The value of x is:", x)
# print("The value of y is:", y)
# print("The value of z is:", z)

# Note: The split() method always returns input values as strings. If you need them as numbers (int or float), you must convert them using typecasting.

# Example of typecasting:
# x,y,z = input("Enter three values:").split()
# x = int(x)  # Convert x to an integer
# y = float(y)  # Convert y to a float
# z = int(z)  # Convert z to an integer
# print("The value of x is:", x)
# print("The value of y is:", y)
# print("The value of z is:", z)

# Change the Type of Input in Python

# By default input() function helps in taking user input as string. If any user wants to take input as int or float, we just need to typecast it.
# Example of taking input as an integer:
# n = int(input("Enter an integer:")) # Taking input as an integer
# print("The value of n is:", n)

# Data Types in python
# print("The type of n is:", type(n))
