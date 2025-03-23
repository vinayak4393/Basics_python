# def a ():
#     x = 10       # x is not defined
#a()
# print(x)     #not possible x is born inside dies inside

# You are defining a function a() that sets a local variable x = 10. 
# However, x is only accessible within the function a() because it is a local variable. 
# When you try to print x outside of the function, you will get a NameError 
# because the variable x is not in the global scope.



x = 20          # global variable
def a():
    x = 10      # local variable

a()
print(x)   # here it takes global variable not local

############

x = 20          # global variable
def a():
    print(x)     # now it access global variable
a()
print(x)

########

# x = 20          # global variable
# def a():
#     x = x+30      # Trying to use x before it's defined locally
#     print(x)     
# a()
# print(x)            # results in an error

################################################################

x = 20              # global variable

def a():
    global x        # declare that we're referring to the global variable x
    x = x + 40      # modify the global x by adding 40 to it
    print(x)        # print the modified value of global x

a()                 # call the function a()
print(x)            # print the modified global x


###########


x = 20  # global variable

def a():
    x = 10  # local variable 'x' inside the function, shadows the global 'x'
    x = x + 40  # modifies the local 'x' (which is 10), so it becomes 50
    print(x)  # prints the local 'x', which is now 50

a()  # call the function, prints 50
print(x)  # prints the global 'x', which remains 20


################################

x = 20  # global variable

def a():
    global x  # this tells Python we're modifying the global variable 'x'
    x = x + 80  # modifies the global 'x', now x becomes 100
    print(x)  # prints the updated global 'x', which is 100

def b():
    global x  # this tells Python we're modifying the global variable 'x'
    x = x + 100  # modifies the global 'x', now x becomes 200
    print(x)  # prints the updated global 'x', which is 200

a()  # call function a(), prints 100
b()  # call function b(), prints 200
print(x)  # prints the global 'x', which is now 200 after both functions have modified it



################################


x = 20  # global variable

def a(x):  # function parameter x
    x = x + 40  # this x is local to the function
    print(x)  # prints local x, which is the function parameter incremented by 40 i.e, 50

a(10)  # passing 10 as an argument, so local x inside the function becomes 10
print(x)  # prints global x, which remains 20

#################################################################################################


x = 20  # global variable

def a(x):  # function parameter x
    x = x + 40  # this x is local to the function
    print(x)  # prints local x, which is the function parameter incremented by 40 ,i.e 60

a(x)  # passing the global variable x (which is 20) to the function
print(x)  # prints global x, which remains 20



























































