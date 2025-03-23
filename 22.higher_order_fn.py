# It takes function as argument and returns function as result



def apply_operation(operation, numbers):
    return [operation(num) for num in numbers]

# Define simple operations
def square(x):
    return x * x

def cube(x):
    return x * x * x

numbers = [1, 2, 3, 4, 5]

# Use apply_operation with square and cube
print(apply_operation(square, numbers))  # [1, 4, 9, 16, 25]
print(apply_operation(cube, numbers))  # [1, 8, 27, 64, 125]







