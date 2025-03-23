"""Different types of arithmatic operators
(+),(-),(*),(/),(//),(%)
"""
num1 = 10
#num1 is identifier and 10 is a value

num2 = num1
#num1 address access is given to num2

num3 = 40
num4 = num1 + num3
#Here num3 gets assigned new address
#Operation is addition

num5 = num3 - num1 #Subtraction

num6 = num1 * num3 #Multiplication

num7 = num3 / num1 #Division

num1 = 3
num8 = num3 // num1 #It is floor division, we get floor value (bottom value) of integer

num9 = num3 % num1 #we get remainder

print("Addition",num4)
print("Subtraction",num5)
print("Multiplication",num6)
print("Division",num7)
print("Floor Division",num8)
print("Remainder",num9)

import math
num10 = 13.999
result = math.ceil(num10)
print("Ceil value",result) #this is to get ceil (top value)


