# a closure is a function that captures the state (variables) from the surrounding scope in which it was created, 
# and can continue to access those variables even after the outer function has finished execution.

# A closure in Python refers to a function object that "remembers" values from its enclosing lexical scope,
# even after the scope has finished executing.

# closure is function that remembers variables from surrounding scope and can access variables 
# even after outer function has finished execution


def outer_function(x):
    # This is the outer function that takes a parameter 'x'
    
    def inner_function(y):
        # This is the inner function that references 'x' from the outer function
        return x + y  # The closure remembers the value of 'x'
    
    return inner_function  # Return the inner function, which is the closure

# Create a closure by calling outer_function
closure = outer_function(10)

# Now, even though outer_function has finished executing,
# the closure still remembers the value of 'x' from outer_function (which was 10).
result = closure(5)  # Pass 'y' as 5
print(result)  # Output will be 15 (10 + 5)

#########################################################################

def outer_function(x):
    # This is the outer function that takes a parameter 'x'
    
    def inner_function(y):
        # This is the inner function that references 'x' from the outer function
        return x ** y  # The closure remembers the value of 'x'
    
    return inner_function  # Return the inner function, which is the closure

# Create a closure by calling outer_function with x = 2
closure = outer_function(2)

# Now calling closure(3) will compute 2 ** 3
result1 = closure(3)  # result1 = 2 ** 3 = 8
print(result1)  # Output: 8


##########################################################################################################



def outer_function(x):
    # This is the outer function that takes a parameter 'x'
    
    def inner_function(y):
        # This is the inner function that references 'x' from the outer function
        return x ** y  # The closure remembers the value of 'x'
    
    return inner_function  # Return the inner function, which is the closure

# Call outer_function with x=2, then immediately call the returned function with y=3
print(outer_function(2)(3))  # Output: 8


##################################################################################################3


def power_of(exponent):
    def power(base):
        return base ** exponent
    return power

# Create power function for exponent 3 (i.e., cube)
cube = power_of(3)

print(cube(2))  # Output: 8
print(cube(4))  # Output: 64


#######################################################


def create_calculator(x):
    def calculate(y, operation):
        if operation == "add":
            return x + y
        elif operation == "subtract":
            return x - y
        elif operation == "multiply":
            return x * y
        elif operation == "divide" and y != 0:
            return x / y
        else:
            return "Invalid operation or division by zero"
    return calculate

# Create a calculator with x = 10
calculator = create_calculator(10)

print(calculator(5, "add"))      # Output: 15
print(calculator(5, "subtract")) # Output: 5
print(calculator(5, "multiply")) # Output: 50
print(calculator(5, "divide"))   # Output: 2.0


###############################


def calc(x):
    def do(y, op):
        if op == "add":
            return x + y
        elif op == "subtract":
            return x-y
        elif op == "multiply":
            return x*y
        elif op == "divide" and y != 0:
            return x/y
        else:
            return "invalid operation or division by zero"
    return do

print(calc(10)(5, "add"))
print(calc(20)(5, "add"))


#################################################################











