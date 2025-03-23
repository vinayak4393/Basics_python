#control flow is in which individual condition are executed
#1.conditonals  2.Loops

#if condition: 
#    <statement> (4 space indentation)
#else:
#    <statement>



# For multiple condition sequentially
#if condition: 
#    <statement> (4 space indentation)
#elif condition:
#    <statement>
#else:
#    <statement>


a, b = 20, 30

if a > b:
    print("a is greatest")
else:
    print("b is greatest")
   

"""
a = input("Enter a number1 \n")
b = input("Enter a number2 \n")
c = input("Enter a number3 \n")

if a > b and a > c:
    print("a is greatest")
elif b > a and b > c:
    print("b is greatest")
else:
    print("c is greatest")
# above case fails if a= 60, b= 200, c= 10 o/p is a is greatest
# because it treats them as strings and checks only first index position that is greater
# Therefore convert them into integer like given below

a = int(input("Enter a number1 \n"))
b = int(input("Enter a number2 \n"))
c = int(input("Enter a number3 \n"))

if a > b and a > c:
    print("a is greatest")
elif b > a and b > c:
    print("b is greatest")
else:
    print("c is greatest")

"""



# nested if 
x = 10
if x > 5:
    if x < 15:
        print("x is between 5 and 15")
    else:
        print("x is greater than 15")
else:
    print("x is less than or equal to 5")


x = 5
if x > 15:
    print("x is greater than 15")
else:    
    if x < 5:
        print("x is less than 5")
    else:
        if x == 5:
            print("x is equal to 5")
        else:
            print("x is between 5 and 15")

x = 16                # using elif conditon
if 5 < x < 15:
    print("x is between 5 and 15")
elif x < 5:
    print("x is less than 5")
elif x == 5:
    print("x is equal to 5") 
else:
    print("x is greater than 15")           



# simple if else
x = 100
if x > 100:
    print("x is greater than 100")
else:    
    print("x is less than or equal to 100")

# now above simple if else is written in one statement like
print("x is greater than 100") if x > 100 else print("x is less than or equal to 100")

#or nested if else
print("x is greater than 100") if x > 100 else print("x is equal to 100") if x == 100 else print("x is less than 100")




# another example
error_log = [
    "Error : Package not installed",
    "Error : Request timeout",
    "Error : file not found"
]
if error_log:
    print("fix the errors")


error_log = []   #If error_log is empty then 
if error_log:
    print("fix the errors")
else:
    print("No errors")


error_log = "   "   #If error_log just contains some spaces
if error_log.strip():
    print("fix the errors")
else:
    print("No errors")


















