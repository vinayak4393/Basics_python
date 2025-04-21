file1 = open('try.py')          # by default it is in read mode
out = file1.read()
print(out)

file1 = open('try.py' , 'r')          # or we can use 'r' then it is in read mode
out = file1.read()
print(out)


file1 = open('try.py' , 'r')          
out = file1.readlines()             # read lines gives it into a list
print(out)


file1 = open('dummy.py' , 'w')          
out = file1.write("Good Morning!!")             # write, it overwrites on whatever content already present
print(out)


# file1 = open('dummy.py' , 'a')
# out = file1.read()                        #'a' is append, read is not supported with a instead use a+
# print(out)

file1 = open('dummy.py' , 'a+')
out = file1.read()                        # 'a+' reads the file in this case
print(out)

file1 = open('dummy.py' , 'a')
out = file1.write('\nToday is a good day!!')         #'a' is append, write in this case appends te file by writing
print(out)

file1 = open('dummy.py' , 'a')
out = file1.write("""\ndict1 = { "a" : 10,
         "b" : 20,
         }
print(dict1)""")         
print(out)

file1 = open('dummy.py' , 'a+')
file1.seek(0)                       # it takes cursor from the starting line
out = file1.read()                        
print(out)


file1.close()           # it is used to close file everytime so less memory is consumed


with open ('dummy.py', 'r') as file1:           #using with class we open and read file no need to close manually everytime
    file1.read()







