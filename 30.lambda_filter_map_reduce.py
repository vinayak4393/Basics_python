# lambda is a small anonymous function defined using lambda keyword
# Anonymous: Lambda functions are usually not assigned to a variable and don’t require a function name.

# Single Expression: Lambda functions can only contain one expression. You can't have multiple statements inside a lambda.

# Inline Usage: Often used inline where a full function definition is not necessary.

# When you need a function for a short operation and don't want to formally define it using def.    
#syntax ==> lambda arguments: expression




add = lambda x, y: x + y
print(add(3, 5))  # Output: 8


square = lambda x: x ** 2
print(square(4))  # Output: 16


###############################################################################

# map function map()

# map is a built in higher order function that 
# allows you to apply a given function to all items in an iterable (such as a list, tuple, etc.)
# and returns a map object (an iterator).

# it helps transform elements in an iterable by applying a function to each item.

# When you want to apply a function to every element in an iterable (list, tuple, etc.) and 
# want a more concise alternative to a for loop.

# using lambda
numbers = [1, 2, 3, 4, 5]

# Using map() to square each number
squared_numbers = map(lambda x: x ** 2, numbers)

# Convert map object to a list and print
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]



# using defined function
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

# Using map() with the square function
squared_numbers = map(square, numbers)

# Convert map object to a list and print
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]




# If multiple iterables are provided, the function will take as many arguments as there are iterables 
# and apply the function in parallel, stopping when the shortest iterable is exhausted.


numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

# Using map() to add elements of two lists
result = map(lambda x, y: x + y, numbers1, numbers2)

# Convert map object to a list and print
print(list(result))  # Output: [5, 7, 9]





#You can also use map() to convert the elements of a list to a different data type. 
#For example, converting a list of strings into integers.

str_numbers = ['1', '2', '3', '4', '5']

# Using map() to convert strings to integers
int_numbers = map(int, str_numbers)

# Convert map object to a list and print
print(list(int_numbers))  # Output: [1, 2, 3, 4, 5]



#####################################################################

# filter function filter()

# The filter() function in Python is a built-in higher-order function that
# allows you to filter elements from an iterable (such as a list, tuple, etc.) based on a given function 
# that evaluates each element to either True or False.

#  The elements for which the function returns True are included in the resulting iterable,
#  while elements for which the function returns False are excluded.

# syntax ==> filter(function, iterable)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using filter() to get only even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Convert filter object to a list and print
print(list(even_numbers))  # Output: [2, 4, 6, 8]


# Using a Named Function:

def is_odd(x):
    return x % 2 != 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using filter() with the is_odd function
odd_numbers = filter(is_odd, numbers)

# Convert filter object to a list and print
print(list(odd_numbers))  # Output: [1, 3, 5, 7, 9]



#Filtering Non-Empty Strings:

strings = ["apple", "", "banana", "cherry", "", "date"]

# Using filter() to remove empty strings
non_empty_strings = filter(None, strings)

# Convert filter object to a list and print
print(list(non_empty_strings))  # Output: ['apple', 'banana', 'cherry', 'date']



# Filtering Negative Numbers:

numbers = [-10, 15, -20, 30, 0, -5, 50]

# Using filter() to get only positive numbers
positive_numbers = filter(lambda x: x > 0, numbers)

# Convert filter object to a list and print
print(list(positive_numbers))  # Output: [15, 30, 50]


#######################################################################

# reduce function reduce()

# The reduce() function in Python is a built-in function in the functools module 
# that allows you to apply a binary function (a function that takes two arguments) cumulatively to the items in an iterable, 
# from left to right, so as to reduce the iterable to a single value.

# syntax ==> from functools import reduce
# reduce(function, iterable, [initializer])


from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using reduce() to find the sum
result = reduce(lambda x, y: x + y, numbers)

print(result)  # Output: 15



from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using reduce() to find the product of numbers
result = reduce(lambda x, y: x * y, numbers)

print(result)  # Output: 120


# Using the initializer Parameter:

from functools import reduce

numbers = [1, 2, 3, 4]

# Using reduce() with an initializer to find the sum
result = reduce(lambda x, y: x + y, numbers, 10)

print(result)  # Output: 20


#Concatenating Strings:

from functools import reduce

strings = ['Hello', ' ', 'World', '!']

# Using reduce() to concatenate the strings
result = reduce(lambda x, y: x + y, strings)

print(result)  # Output: 'Hello World!'














