# It's a way to wrap additional functionality around a function without modifying its actual code.

# A decorator in Python is a function that takes another function (or method) as an argument and 
# adds some kind of functionality to it, 
# returning a new function that usually extends or alters the behavior of the original function.


# A decorator is a function that modifies or enhances the behavior of another function.
# It allows you to wrap another function and add extra functionality to it, such as logging, timing, access control, etc.,
# without modifying the function's code directly.


# It will take a function as an argument and return a new function that adds additional behavior.

# decorator is function that takes another function as input and returns a new function 
# that typically extends or modifies the behavior of the original function.



# Visualizing the Call Stack:
# greet() (actually wrapper()) is called.
# Print "Function is about to be called!"
# Call greet().
# greet() is called (prints "Hello!").
# Return from greet().
# Control goes back to wrapper().
# Print "Function has been called!".
# Return from wrapper().

# Step 1: Define the decorator
def my_decorator(func):
    def wrapper():
        print("Function is about to be called!")
        func()  # Call the original function
        print("Function has been called!")
    return wrapper

# Step 2: Apply the decorator using the @ symbol
@my_decorator          #equivalent to ==> greet = my_decorator(greet)
def greet():
    print("Hello!")

# Call the decorated function
greet()

# my_decorator(func): This is the decorator function that takes another function (greet) as an argument.

# wrapper(): The wrapper function is defined inside the decorator. 
# It adds extra behavior (in this case, print statements before and after the function call), 
# then calls the original function (func()).

# @my_decorator: This is the decorator syntax, which is equivalent to greet = my_decorator(greet).
# The greet function is now wrapped by the wrapper function.

# When you call greet(), it first prints "Function is about to be called!",
# then calls the original greet() function (which prints "Hello!"), and finally prints "Function has been called!".



def wrapper(abc):
    abc()  # Call the function passed as 'abc' inside the wrapper

def greet():
    print("test wrapper!!")  # The function to be passed to 'wrapper'

x = greet
wrapper(x)  # Pass 'greet' function as an argument to 'wrapper'


##########################################################################################


def deco(xyz):
    def wrap(*args):
        result = xyz(*args)  # Call the original function with arguments
        return result  # Return the result
    return wrap  # Return the wrapped function

def add(a, b):
    return a + b  # Simple function that adds two numbers

# Apply the decorator to the 'add' function
out = deco(add)

# Call the decorated function using 'out'
print(out(20, 30))  # Output the result of calling 'add(20, 30)'

# Call the decorator directly without saving it to a variable
print(deco(add)(50, 60))  # Output the result of calling 'add(50, 60)'


#######################################################################################


def deco(xyz):
    def wrap(*args):
        print("Operation is done")
        result = xyz(*args)  # Call the original function with arguments
        return result  # Return the result
    return wrap  # Return the wrapped function

# Apply the decorator using the @ syntax ==> add = deco(add)
@deco
def add(a, b):
    return a + b  # Simple function that adds two numbers

# Now you can call the decorated function directly
print(add(20, 30))  # Output the result of calling 'add(20, 30)'

# Call the decorator directly without saving it to a variable
print(deco(add)(50, 60))  # Output the result of calling 'add(50, 60)'


#####################################################################################


def deco(xyz):
    def wrap(*args):
        result = xyz(*args)  # Call the original function with arguments
        return result  # Return the result
    return wrap  # Return the wrapped function


def add(a, b):
    return a + b  # Simple function that adds two numbers

def sub(a, b):
    return a - b

print(add(100, 60))

# Call the decorator directly without saving it to a variable
print(deco(add)(100, 60))  # Output the result of calling 'add(50, 60)'

print(deco(sub)(100, 60))

print(add(100, 60))



########################################################################################



def requires_authentication(func):
    def wrapper(username, password):
        if username == "admin" and password == "password123":
            print("Authentication successful!")
            return func(username)
        else:
            print("Authentication failed!")
    return wrapper

@requires_authentication
def access_dashboard(username):
    print(f"Welcome to the dashboard, {username}!")

access_dashboard("admin", "password123")  # Should succeed
access_dashboard("user", "wrongpassword")  # Should fail



#######################################################################################



def multiply_return_value(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2  # Multiply the return value by 2
    return wrapper

@multiply_return_value
def add(a, b):
    return a + b

print(add(5, 10))  # The result of 5 + 10 will be multiplied by 2






























