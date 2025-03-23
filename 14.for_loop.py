# for loop
# loops are used to execute a block of code multiple times.
# loops allows you to repeat a block of code as long as certain condition is true

key = "devops" 

for element in key:
    print(element)




key = "devops"

for element in key:
    element = element.upper()       # to convert it to uppercase
    print(element)



key = "devops"
new_key = ""

for letter in key:
    new_key += letter        # to concatenate all the letters 

print(new_key)




key = "devops"
new_key = ""

for letter in key:
    if letter == "d" or letter == "o":
        letter = letter.upper()                
    new_key += letter                          # after coming out of if condition but inside for loop

print(new_key)





key = "devops"
new_key = ""

for letter in key[:2]:
    if letter == "d" or letter == "o":
        letter = letter.upper()                
    new_key += letter                          

print(new_key)





seq = [2, 3, 4, 5, 6, 77, 44, 789, 26, 48, 2925]
output = []
for el in seq:
    output.append(el ** 2 + 3)
print(output)    



seq = [2, 4, 8]
for pos, el in enumerate(seq):                # pos is index position and el is element enumerate must be used
    print(f"{pos} ==> {el}")





# secret = 5689
# for trial in range(3):
#     pin = input("print enter PIN \n")
#     if pin == secret:
#         print("Good, correct PIN \n")
#         break                           # It breaks the for loop 
  


candidates = ["CSE", "ECE", "BCA", "CIVIL", "ISE", "ELE", "MECH"]
rejected = ["CIVIL", "ELE", "MECH"]

for el in candidates:
    if el in rejected:
        continue
    print(f"{el} submit your documents!!")



lst = []
for x in range(10):
    lst  += [x]       # add range of 10 in list
print(lst)
print("Executed!!")    



lst = ""
for x in range(10):
    lst += str(x)   # It converts to string and concatenates 
print(lst)
print("Executed!!") 


data = []
for el in data:          #it didnt print hello becoz no element in data as it is falsy value
    print("hello")
print("executed")    
   

data = [1, 2, 3]
for el in data:              #it takes list length and prints hello thrice and executed once
    print("hello")                      
else:
    print("Executed")



data = [1, 2, 3]
for el in data:              #it takes element length and prints hello once breaks
    print("hello") 
    break                      # due to break statement else doesnot print s it entirely comes out for loop
else:
    print("Executed")



# data = [server1, server2, server3]
# for el in data:
#     if not el.working:
#         <some_server_not_work> = True
#         break
#     else:
#         print("executed")



states = ["Bihar", "Goa", "Assam"]
capital = ["Patna", "Panaji", "Dispur"]

data = dict(zip(states, capital))
print(data)


states = ["Bihar", "Goa", "Assam", "MP"]   #MP is not considered
capital = ["Patna", "Panaji", "Dispur"]

data = dict(zip(states, capital))
print(data)

for states, capital in data.items():
    print(f"Capital city of {states} is {capital}")




# List comprehension ==> It is concise way to generate lists , one line for generating lists

num = [2, 4, 6, 8]
num1 = [el ** 2 for el in num]
print(num1)


tech = ["Linux", "AWS", "Python"]
cap_tech = [el.upper() for el in tech]
print(cap_tech)

# last = [tech.pop() for el in tech]
# print(last)

even_num = [x for x in range(10) if x % 2 == 0]
print(even_num)



# if nested loops
tech1 = ["Linux", "Python", ["gcp", "aws"]]
tech2 = []
for data in tech1:
    if isinstance(data, str):
        tech2.append(data.upper())
    elif isinstance(data, list):
        for el in data:
            tech2.append(el.upper())            
print(tech2)
















