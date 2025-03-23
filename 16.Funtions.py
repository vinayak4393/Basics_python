# It is reusable block of code that performs specific task
# camel case is usually used

def add2Num(x,y):
    out = x + y
    return out

result = add2Num(20,30)
print(result)

tech = ["python", "linux", "aws"]
def capital():
    out = [el.upper() for el in tech]
    print(f"list in upper case ==> {out}")

capital()



def capital(input_lists):
    out = []
    for el in input_lists:
        out.append(el.upper()) 
    return out

tech = ["python", "linux", "aws"]
lang = ["java", "c"]
prog = ["kube", "docker", "jenkins"]
print(capital(tech))
print(capital(lang))
print(capital(prog))


def greet():
    pass       # it is used to indicate still code needs to be written


def greet():
    x = 10
    return       # returns none 
out = greet()
print(out)


def greet():
    x = 10
    return None   # still same
out = greet()
print(out)



def greet():
    x = 10
    return x       # gives 10
out = greet()
print(out)


def greet():
    x = 10
    return 
    x             # It is silent gives none
out = greet()
print(out)


def greet():
    x = 10
    return (
    x )            # gives 10 again
out = greet()
print(out)


# multiple values return

def greet():
    x = 10
    y = 20
    return x, y    # using comma makes it into a tuple
out = greet()
print(out)


lst1 = ["aws", "gcp", "azure"]
lst1.sort()          # sort is used to sort based on ASCII value
print(lst1)



def greet(abc):                 # parameter used 
    print(f"Hi {abc}, Good Morning!!")

visitor1 = "Messi"
visitor2 = "Ronaldo"

greet(visitor1)
greet(visitor2)




def greet(abc = "visitor"):                 # default argument is used 
    print(f"Hi {abc}, Good Morning!!")

visitor1 = "Messi"
visitor2 = "Ronaldo"

greet(visitor1)
greet(visitor2)                              
greet("rahul")
greet()                                        # default visitor is used 





#   Named arguments

def selfIntro():
    name = "Messi"
    place = "Argentina"
    skill = "Football"

    print(f"Hi I am {name}, I am from {place}, I am good at {skill}")

selfIntro()



def selfIntro(name, place, skill):
    print(f"Hi I am {name}, I am from {place}, I am good at {skill}")

selfIntro("Messi", "Argentina", "Football")




# def selfIntro(name, place = "Argentina", skill):         
#     print(f"Hi I am {name}, I am from {place}, I am good at {skill}")    

# selfIntro("Messi", "Football")    # o/p error there needs to be argument 

 #Either default argument needs to be at last (no argument, default arg, no argument  ==> not possible)


def selfIntro(name, place = "Portugal", skill = "Dancer"):
    print(f"Hi I am {name}, I am from {place}, I am good at {skill}")

selfIntro("Ronaldo") 


def selfIntro(name, place = "America", skill = ""):
    print(f"Hi I am {name}, I am from {place}, I am good at {skill}")

selfIntro(name = "Trump", skill = "Real_estate")     # We can write complete parameter and its argument



def selfIntro(name, place = "America", skill = ""):
    print(f"Hi I am {name}, I am from {place}, I am good at {skill}")

selfIntro(skill = "Real_estate", name = "Trump")     # even if jumbled it is correct





def addNum(data):
    sum = 0
    for el in data:
        sum += el
    print(sum)

lst1 = [20, 30, 40]
addNum(lst1)



# def lstAdd(data):
#     sum = []
#     for el in data:
#         sum.append(el + 10)
#     print(sum)

# lstAdd(10,30)                 # we get error as multiple arguments needs to be passed so we use *data



def lstAdd(*data):                # *Argument is used for multiple elements                           
    sum = []
    for el in data:
        sum.append(el + 10)
    print(sum)

lstAdd(10,30) 




# to use shallow copy

def intro(data):
    data.append(100)
    print(data)

lst1 = ["abc", "def"]
intro(lst1)


def changeUpper(data):
    newdata = []
    for el in data:
        newdata.append(el.upper())
    print(newdata)

lst2 = ("lks", "fgh")
changeUpper(lst2)    


# now if we want use both together 

# def changeUpper(data):
#     newdata = []
#     for el in data:
#         newdata.append(el.upper())
#     print(newdata)



# def intro(data):
#     data.append(100)
#     print(data)

# lst1 = ["abc", "def"]

# intro(lst1)                     # Error because of integer used and different data type to avoid use copy()
# changeUpper(lst1)  




def changeUpper(data):
    newdata = []
    for el in data:
        newdata.append(el.upper())
    print(newdata)



def intro(data):
    temp = data.copy()     # copy() as it creates different address so no problem here we use temp variable
    temp.append(100)
    print(temp)

lst1 = ["abc", "def"]

intro(lst1)                     
changeUpper(lst1)  



# to pass function inside a function
def b():
    print("Im inside function B")

def a():
    print("Im inside function A")
    b()

a()



# Recursive function ==> It calls itself to solve a problem

#factorial of 5
fac = 1
for i in range(1, 6):
    fac *= i
print(fac)

# above using recursive function can be
 
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

out = factorial(10)
print(out)


# for sum of n numbers

def sumNum(num):
    if num == 0:
        return 0
    return num + sumNum(num - 1)

out = sumNum(10)
print(out)























