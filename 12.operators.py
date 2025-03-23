# Operators are special symbols or keywords used to perform operation on values or variables.
# Arithmatic Operators
# Comparison Operators
# Logical Operators
# Bitwise Operators
# Assignment Operators
# Identity Operators
# Membership Operators
# Ternary Operators

# Comparison Operators
num1, num2 = 10, 20
print(num1>num2)

print(num1<num2)

print(num1==num2)

print(num1>=num2)

print(num1<=num2)

print(num1!=num2)


# Logical Operator
a, b, c = 10, 20, 30
print(a > b and a > c)

print(c > a and c > b)

print(a > b or a > c)

print(c > a or c > b)

# not



#Bitwise Operator
a, b = 5, 3
print(a & b)   # (5 ==> 0101 AND 3 ==> 0011 {TTT})

print(a | b)  # (5 ==> 0101 OR 3 ==> 0011 {FFF})

print( ~ a)  #  (5 ==> 0101 NOT of 5 ==> -6 )

print(a ^ b)  #  (^ ==> XOR  {5 ==> 0101 XOR 3 ==> 0011  o/p is 6 ==> 0110})

print(a << 1)  # Shift bits to the left by 1 position: 1010 in binary (10 in decimal)
 # Output: 10

a = 5  # 0101 in binary

print(a >> 1)  # Shift bits to the right by 1 position: 0010 in binary (2 in decimal)
  # Output: 2


# we can use bitwise operator in sets
a = {1, 2, 3}
b = {2, 5, 6}
#a - b = {1, 3}
print(a.difference(b)) 
print(a.intersection(b))
print(a > b) # To check a is superset of b

c = {1, 2, 3, 4, 5, 6}
d = {1, 2, 3}
print(d < c)  # To check d is subset of c




# Assignment Operataor
a = 10 
b = 100
print(a==b)

a += 5 # a = a + 5 {add and assign}
print(a)

a -= 5 # a = a - 5 {subtract and assign}
print(a)

a *= 3 # a = a * 3 {multiply and assign}
print(a)

a /= 10 # a = a / 10 {divide and assign}
print(a)

a **= 3 # a = a ** 3 {exponentation and assign}
print(a)

a //= 3 # a = a // 3 {floor and assign (27/3)}
print(a)

a %= 8 # a = a % 3 {remainder and assign}
print(a)



# Identitiy Operator
# used to compare the memory location of 2 objects
# is supports lists, tuples, sets, dict

a = {"ABC", 1, 2}
b = {"ABC", 1, 2}
print(a is b) # is used to check whether both have same address (here different address) {false}
print(a is not b) # is not {true}

b = a
print(a is b) #now both have same address {true}
print(a is not b) #false




# Membership Operator

fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)  # Output: True
print('orange' not in fruits) #Output: True









