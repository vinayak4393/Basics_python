str1 = """A sell-off in global stocks eased in Europe on Tuesday
following a sharp fall in US stocks that came as 
raised concerns about the negative economic impact of 
President Donald Trump's tariffs."""

out = str1.upper() #It makes entire in string in upper case
print(out)

print(str1.lower()) #It makes entire in string in lower case

print(str1.count("in")) #It count the number of occurence 

print(str1.find('in'))  #It finds the first occurence of word from left side by default
print(str1.rfind('in')) #It finds the from right side which gives us last occurence of word

print(str1.replace('stocks','shares')) #It replaces all occurences of word 

print(str1.partition('raised')) #It divides them into parts 3 parts ==> selected word,left of that word,right of that word
print(str1.partition('stocks')) #It divides only with first occurence of word

str2 = "VERSION-2.0.12-NEW PYTHON"

#first_option = nam[0]  VERSION ==> [0]
#second_option = nam[1]  2.0.12 ==> [1]
#third_option = nam[2]   PYTHON ==> [2]


print(str1.split(" ")) #It splits the string with space in a list
print(str2.split("-")) #It splits the string with hyphen(-) in a list
nam = str2.split("-") #It splits the string with hyphen(-) in a list

print(nam[0]) #It prints only the first_option after split is performed

str3 = "VERSION2.13.34-NEW PYTHON" 
str4 = "VERSION12.13.34-NEW PYTHON"

print(str3>str4) #It shows true even though str4 is greater 
#only first character is compared therefore it thinks str3 is greater

new = "2.13.34"
print(new.zfill(10)) #To rectify line 37 problem we use zero fill and it fill initially with zero


print(((str3.split("-"))[0].replace("VERSION",'')).zfill(10)) # we can combine use this way
print(((str4.split("-"))[0].replace("VERSION",'')).zfill(10))
nam1 = ((str3.split("-"))[0].replace("VERSION",'')).zfill(10)
nam2 = ((str4.split("-"))[0].replace("VERSION",'')).zfill(10)
print(nam1>nam2) #now it says false as the above problem is rectified. 


#below same process is done in more cleaner way
print(str3.split("-")) #It splits it into 2 portions

out1 = str3.split("-")[0] #To get only first portion
print(out1)

out2 = (out1.replace("VERSION",'')) #subsequently in first option VERSION is replaced with nothing
print(out2)

out3 = (out2.zfill(10)) #here the number is filled with zeroes to compare
print(out3)
#similarly for str4 you can do it and get it.

#To remove characters in a string we use strip

vin1 = "   02.13.34    "
print(vin1.rstrip()) #To remove right spaces
print(vin1.lstrip()) #To remove left spaces

vin2 = "excellent"
print(vin2.strip('e')) #It will strip only first occurence of 'e' of duplicate char

#To extract do string slicing
txt1 = "Michael Jordan"
print(txt1[0:5]) #To extract character from index pos 0 till 4 

#To join string we can concatenate or use join
text1 = "Michael"
text2 = "Jordan"
print("#- ".join([text1,text2]))






