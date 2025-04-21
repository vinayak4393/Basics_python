# # 1. Basic Loop
# # Write a Python program that prints the numbers from 1 to 10 using a for loop.

# for i in range(1,11):
#     print("numbers from 1 to 10\n", i)

# out = []
# for i in range(1,11):
#     out.append(i)
# print("numbers from 1 to 10 in list\n", out)


# # 2. Sum of Numbers
# # Write a Python program that calculates the sum of numb
# # 
# # ers from 1 to 100 using a for loop.

# key = [100]
# for i in key:
#     out = (i*(i+1))/2
# print(out)

# for i in range(1,101):
#     result = (i*(i+1))/2
# print(result)

# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print(sum)


# 3. Multiples of 5
# Write a Python program that prints all multiples of 5 between 1 and 50 using a for loop.

# 5,10,15
# out = []
# for i in range(1,51):
#     if i % 5 == 0:    
#         out.append(i)
# print(out)        

# for i in range(5,51,5):
#     print(i)



# 4. Reverse Count
# Write a Python program that prints the numbers from 10 down to 1 using a for loop.

# for i in range(10,0,-1):
#     print(i)


# 5. Factorial Calculation
# Write a Python program that calculates the factorial of a number (input by the user) using a for loop.

# num = int(input("Enter a number:"))

# el = 1
# for i in range(num):
    
#     el = el * num
#     num -= 1

# print(el)

# n = int(input("Enter a number:"))
# for i in range(n-1,0,-1):
#     n = n * i
# print(n)

# if n = 5, the range() function will generate the following sequence of values for i:
# First iteration: i = 4
# The current value of n (which is 5) is multiplied by i (which is 4), so n becomes 5 * 4 = 20.
# On the second iteration of the loop:
# i = 3
# The current value of n (which is now 20) is multiplied by i (which is 3), so n becomes 20 * 3 = 60.


# num = int(input("Enter a number:"))
# factorial = 1
# for i in range(1,num+1):
#     factorial = factorial * i
# print(el)

#its always best to initialize factorial instead of modifying num value 



# 6. Even or Odd
# Write a Python program that checks whether a number (input by the user) is even or odd, and prints the result. 
# Use a for loop to iterate through a given range of numbers and print whether each number is even or odd.

# num = int(input("Enter a number: "))
# # if num % 2 == 0:
# #     print("Even number")
# # else:
# #     print("Odd number")    


# for i in range(num,1,-1):
#     if i % 2 == 0:
#         print(f"{i} is an even number")
#     else:
#         print(f"{i} is an odd number")    



# 7. Prime Numbers
# Write a Python program that prints all the prime numbers between 1 and 50 using a for loop.

# 2,3,5,7
# divisible by only 1 and itself
# for num in range(2,51):
#     prime = True
#     for i in range(2,num):
#         if num % i == 0:
#             prime = False
#             break
#     if prime:
#         print(num)


# # By number input by use check prime
# num = int(input("Enter a number : "))
# prime = True
# for i in range(2,num):
#     if num % i == 0:
#         prime = False
#         break

# if prime and num > 1:
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")        


# 8. Fibonacci Sequence
# Write a Python program that prints the first n Fibonacci numbers,
# where n is input by the user, using a for loop.

0,1,1,2,3,5,8
num = num-1 + num-2

num = int(input("Enter a number : "))
a, b = 0, 1
for i in range(num):
    




