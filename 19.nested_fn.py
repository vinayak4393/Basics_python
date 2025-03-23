# def a():
#     def b():
#         print("Good Day!!")

# a()             ## Calling function a() 
# print(a())     ## Calling function a() again, but trying to print its return value

# Inside a(), you define another function b(). 
# However, you don't call b() inside a(), so it doesn't do anything when a() is called.
# The function a() doesn't have a return value, so when a() is called, it implicitly returns None.

# When you call a(), it doesn't print anything because b() is not called inside a(), and a() doesn't return anything.
# So, it implicitly returns None, and that result is discarded.

########################################################

def a():
    def b():
        print("Good Day!!")
    b()         # Calling function b() inside a()

a()             # Calling function a() 
print(a())      # Calling function a() again, but trying to print its return value which is none

# Even though a() calls b() and prints "Good Day!!",
# since a() itself doesn't return a value, the result of calling a() is None.


###################################################

def a():
    pass

print(a)         # Prints the function object itself

# <function a at 0x000001CC28193D96> (something like this output)

################################

count = 0  # global variable

def a():
    global count  # Declare that we are using the global variable 'count'
    count += 1  # Increment the global variable 'count' by 1

print(a())  # Call function a(), but it doesn't return anything
print(count)  # Print the updated value of the global variable 'count'


##########################################################

count = 0  # global variable

def a():
    global count  # Declare that we are using the global variable 'count'
    count += 1  # Increment the global variable 'count' by 1

out = a()  # Call function a() and store its return value in 'out'
print(out)  # Print the value of 'out'
a()  # Call function a() again
print(count)  # Print the updated value of the global variable 'count'


#############################################################################


count = 0  # global variable

def a():
    global count  # Declare that we are using the global variable 'count'
    count += 1  # Increment the global variable 'count' by 1

out = a  # Store function a() in 'out' (but not call it yet)
out()  # Call function a() through 'out'
out()  # Call function a() again through 'out'
out()  # Call function a() again through 'out'
out()  # Call function a() again through 'out'
print(count)  # Print the updated value of the global variable 'count'







































