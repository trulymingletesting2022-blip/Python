# In Python, variables are used to store data that can be referenced and manipulated during program execution. A variable is essentially a name that is assigned to a value.

# Unlike Java and many other languages, Python variables do not require explicit declaration of type.
# The type of the variable is inferred based on the value assigned.

# Rules for Naming Variables
# To use variables effectively, we must follow Python’s naming rules:

# 1. Variable names can only contain letters, digits and underscores (_).
# 2. A variable name cannot start with a digit.
# 3. Variable names are case-sensitive like myVar and myvar are different.
# 4. Avoid using Python keywords like if, else, for as variable names.

# Below listed variable names are valid:
# age = 23
# _colour = "red"
# total_score = 95.5

# Below listed variables names are invalid:
# 1name = "Error"  # Starts with a digit
# class = 10       # 'class' is a reserved keyword
# user-name = "Doe"  # Contains a hyphen

# Assigning Values to Variables
# In Python, you can assign values to variables using the assignment operator (=).
# Basic assignment:
# x = 10
# y = "Hello"
# z = 3.14
# Multiple assignments:
# Assigning Same Value: Python allows assigning the same value to multiple variables in a single line, which can be useful for initializing variables with the same value.
# a = b = c = 5
# print(a,b,c)
# Dynamic Typing: Python variables are dynamically typed, meaning the same variable can hold different types of values during execution.
# x = 10
# print("The value of x is:", x)
# x = "Hello"
# print("The value of x is:", x)
# Assigning Different Values: We can assign different values to multiple variables simultaneously, making the code concise and easier to read.
# a,b,c = 1, "Python", 3.25
# print("The value of a is:", a)
# print("The value of b is:", b)
# print("The value of c is:", c)

# Type Casting a Variable
# Type casting is the process of converting a variable from one data type to another. In Python, we can use built-in functions like int(), float(), str() to perform type casting.
# Example of type casting:
#s = "123"  # s is a string
#n = int(s)  # n is now an integer
#f = float(n)  # f is now a float
# print("The value of s is:", s)
# print(f"The type of s is: {type(s)}")
# print("The value of n is:", n)
# print("The type of n is:", type(n))
# print("The value of f is:", f)
# print("The type of f is:", type(f))

# Type of variable in Python
# In Python, the type of a variable is determined at runtime based on the value assigned to
# it. You can check the type of a variable using the built-in type() function.
# Example:
# x = 10
# print("The value of x is:", x)
# print("The type of x is:", type(x))
# y = "Hello"
# print("The value of y is:", y)
# print("The type of y is:", type(y))
# z = 3.14
# print("The value of z is:", z)
# print("The type of z is:", type(z))
# li = [1, 2, 3]
# print("The value of li is:", li)
# print("The type of li is:", type(li))
# d = {'key': 'value'}
# print("The value of d is:", d)
# print("The type of d is:", type(d))
# b = True
# print("The value of b is:", b)
# print("The type of b is:", type(b))

# Concept of Object Reference

# In Python, variables are references to objects in memory. When you assign a value to a variable, you are actually creating an object in memory and the variable holds a reference to that object. This means that when you assign one variable to another, both variables refer to the same object in memory.
# Example:
# a = [1, 2, 3]  # a is a reference to a list object
# b = a  # b is now a reference to the same list object
# print("The value of a is:", a)
# print("The value of b is:", b)
# a.append(4)  # Modifying the list through variable a
# print("After modifying a:")
# print("The value of a is:", a)
# print("The value of b is:", b)  # b reflects the change because it references the same object

# # Now we write a = "Hello"  # a now references a new string object
# a = "Hello"
# print("After reassigning a:")
# print("The value of a is:", a)
# print("The value of b is:", b)  # b still references the original list object
# # Now we write b = "World"  # b now references a new string object
# b = "World"
# print("After reassigning b:")
# print("The value of a is:", a)  # a still references the string "Hello"
# print("The value of b is:", b)  # b now references the string "Worldh"
# # But the The original object i.e. the list [1, 2, 3, 4] no longer has any references and becomes eligible for garbage collection.

# # Deleting a Variable
# # In Python, you can delete a variable using the del statement. This removes the reference to the object that the variable was pointing to. If there are no more references to that object, it becomes eligible for garbage collection.
# # Example:
# x = 10
# print("The value of x is:", x)
# del x  # Deleting the variable x
# print("The value of x is:", x)  # This will raise a NameError

# Swapping two variables in Python
# In Python, you can swap the values of two variables in a single line using tuple unpacking. This is a convenient and efficient way to swap values without needing a temporary variable.
# Example:
# a, b = 5, 10
# print("Before swapping: a =", a, "b =", b)
# a, b = b, a  # Swapping the values of a and b
# print("After swapping: a =", a, "b =", b)

# Note: The above method of swapping is specific to Python and is not available in all programming languages. In other languages, you may need to use a temporary variable to achieve the same result.

# Counting Characters in a String
# In Python, you can count the number of characters in a string using the len() function.
# Example:
s = "Hello, World!"
print("The string is:", s)
print("The number of characters in the string is:", len(s))
# Note: The len() function counts all characters in the string, including spaces and punctuation.