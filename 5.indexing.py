"""[start:end:step] [1:5:2]
start will select from 1st character
end will select until 5th charcter means only till 4th character is selected
step will skip to next character
space is also a character """

name = """ABCDEFGHIJKLMN"""


print(name[1:14:2])
print(name[:7])   #It prints 1st to 6th character 
print(name[5:])   #It prints starting from 5th character
print(name[:-1])  #It prints all character but 1
print(name[-2:])  #It prints last 2 character
print(name[:])    #It prints entire thing
print(name[::2])  #It steps(skips_1) 2 characters
print(name[::-1]) #It reverses the character
print(name[::-2]) #It reverses and steps(skips_1) 2 characters



