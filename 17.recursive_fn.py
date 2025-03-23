# factorial
fac = 1
def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)
    
num = 5
out = factorial(num)
print(out)    


# fibonacci
# 0,1,1,2,3,5,8
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo (n - 2)
    
n = 6
out = fibo(n)
print(out)


# sum of n numbers
def sumNum(n):
    if n <= 0:
        return 0
    else:
        return n + sumNum(n-1)

n = 6
out = sumNum(n)
print(out)


# power of a number
# x^n
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power (x, n-1)

x = 2
n = 6
out = power(x, n)
print(out)


# reverse string



