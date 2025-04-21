# Modules are simply files containing Python code that define functions, classes, and variables.
# A module allows you to organize and reuse code in a modular way,
# making your programs more efficient and easier to maintain.


# Types of Modules:

# Standard Library Modules: These are built-in modules provided with Python, such as os, sys, math, datetime, etc.

# Third-Party Modules: These modules are not included in the standard library, 
# but can be installed via package managers like pip (e.g., requests, numpy, pandas).
# pip requests helps for https

# A package is essentially a directory that contains a special __init__.py file
# (which can be empty or contain initialization code) and other Python modules or sub-packages.

# Custom Modules: You can create your own modules by saving Python code in a .py file,
# which can be imported into other Python files.


import my_math
num1 = int(input('Enter a number\n'))
num2 = int(input('Enter another number\n'))

sum1 = my_math.add(num1, num2)    # need to use my_math.(module_name)
print(f"Addition of 2 numbers is {sum1}")


from my_math import sub          # By using this, there is no need to my_math.(module_name) infront   
sub1 = sub(num1, num2)
print(f"Subtraction of 2 numbers is {sub1}")



from my_math import *          # to import all functionalities we use *
prod = mul(num1, num2)
div1 = div(num1, num2)


print(f"Multiplication of 2 numbers is {prod}")
print(f"Division of 2 numbers is {div1}")








