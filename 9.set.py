# set unordered collection of heterogenous data types
# NO duplicates are considered
# uses curly braces

set1 = {'linux',565, 0, 565, 'python', 'AKS'}
print(set1) #doesnot give duplicate elements

# can use - operator symbol subtract duplicate elements from 2 sets
folder1 = {"Linux", "AKS", "Python"}
master_folder1 = {"JAVA", "C", "Python"}
out = folder1 - master_folder1
print(out)


# 2sets cannot be concatenated (+)

#union (combine) remembered like in wenn diagram AUB ==> A union B
folder1 = {"Linux", "AKS", "Python"}
master_folder1 = {"JAVA", "C", "Python"}
out = folder1.union(master_folder1)  #It is used to combine sets doesnot take duplicate elements
print(out)

#intersection (common element) remembered like in wenn diagram  ==> A intersection B
folder1 = {"Linux", "AKS", "Python"}
master_folder1 = {"JAVA", "C", "Python"}
out = folder1.intersection(master_folder1)
print(out)

# pop to remove any element randomly as it is unordered collection
folder1 = {"Linux", "AKS", "Python"}
folder1.pop()
print(folder1)


# remove
folder1 = {"Linux", "AKS", "Python", "AKS"}
folder1.remove("AKS") #Here it removes all occurences of element unlike list
print(folder1)


# add 
folder1 = {"Linux", "AKS", "Python"}
folder1.add("JAVA")
print(folder1)







