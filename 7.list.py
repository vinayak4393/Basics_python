# List is ordered, heterogenous and duplicate collection of data types. It is mutable(can modify)
# list uses square braces
 
lst1 = [1,2,2,"good",2.5,True,None]

print(lst1)

lst2 = "Lionel Messi"
lst2 = lst2.split() #Split using by default space it will be in list
print(lst2)

#lst2 = lst2.split('') cannot split emptily
lst2 = list(lst2) #or use built in funstion list
print(lst2)

# range

print(range(10)) #gives only 1 and 10

txt1 = list(range(10)) #used generate and convert it into list
print(txt1)

# append

tech = ["Linux","Docker","Cloud"]
print(tech)

tech.append("Jenkins") #to add element at the end 
print(tech)

tools = tech #both have same address
print(id(tools))
print(id(tech))

tools.append("kubernates")
print(tools)
print(tech) #It get appended in both tools and tech 

#To avoid above problem we use shllow copy
tools = tech.copy() #different address only tools is appended but not tech



tech = ["Linux","Docker","Cloud"]

# insert
tech.insert(1,"VS code") #index position and element that is to be inserted
print(tech)
tech2 = ["Ansible","Kube"]
tech[1:1] = tech2 #It is another way of inserting using index position
print(tech)



 # extend
cloud1 = ["AWs","GCP","Azure"]
lang1 = ["python","python","JAVA",]
cloud1.extend(lang1) #It extends list with another list even with duplicate elements 
print(cloud1)

#index position usage
print(cloud1[2]) # it gives index 2
print(cloud1[0:2]) 

#every element has its own address
cloud1[2] = "Oracle" #It replaces Azure 
print(cloud1)

#nested list is one or more list inside a list
football = ["pele","maradona",["messi","ronaldo"]]

servers = ["AWS","GCP"]
servers1 = servers #both have same address
dev = ["C", "python",servers]
servers.append("Oracle")
print(servers)
print(dev) #even if change is done in servers it is reflected it shows in dev also

servers1.append("AKS")
print(servers) #both servers and servers1 have same address
print(dev)

servers = ["Azure"]
print(servers)
print(dev) # here servers is modified but not reflected in dev old value is itself taken

#To access element in list
age = [23,56,23,[18,16,17]]
print(age[1])
print(age[3][1])


#remove
age.remove(23) # removes elements on only first occurence
print(age)

age.pop() #by default last index position in current list is removed
print(age)
age.pop(1) #by indexing we can remove particular element
print(age)

output = ["Error",
           "Info",
           "Error"]

out = output.count("Error") #To count the no of occurence of element  
print(out)


# clear
teach = ["Linux","Python","AWS",]
teach.clear() #just empties the entire list, cant use indexing or element
print("EMpty the list", teach)

# delete (It can be used for any data type)
teach = ["Linux","Python","AWS",]
del teach[1] #can delete by indexing 
print(teach)
del teach #deletes everything

nested_list = [[121, 456, 789],
               [000, 111, 222],
               [999, 888, 777]]  #It looks like matrix but it is nested list

nested = [[123, 456, "MIKE"],[],789]
print(nested[0][2][3]) #TO access letter E in MIKE





