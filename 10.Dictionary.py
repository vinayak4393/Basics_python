#Dictionary is ordered collection of key value pairs like set no duplicate element

dict1 = {
        "key" : "value",
        "key" : "value",
        "key" : "value",
        "key" : "value",
}


# empty set is considered as dictionary
set1 = {}
print(type(set1))


EC2 = {
      "pem_key" : "name.pem",
      "type" : "t2micro",
      "AMI" : 40,
      "volume" : "30GB" ,
      }

print(EC2["type"]) #always use square braces to check

#print(EC2["security"]) this gives error instaed of saying none is present

print(EC2.get("Security",)) #it just says none (we get no error)

print(EC2.get("security", "not allocated")) # it says not allocated if not present in dictionary of EC2

print(EC2.get("type", "not allocated")) #it gives t2micro 


EC2 = {
      "pem_key" : "name.pem",
      "pem_key" : "key2.pem",
      "type" : "t2micro",
      "AMI" : 40,
      "volume" : "30GB" ,
      }

print(EC2) #It always takes key pair that is alloted recently

print(EC2.keys()) #just gives all keys
print(EC2.values()) #gives all values

print(list(EC2.keys())) #It prints keys in form of list
print(list(EC2.values())) #It prints values in form of list

print(list(EC2.items())) #we get key value pairs in form of list of tuple

out = list(EC2.items())
print(out[2][0]) 

EC2 = {
      "pem_key" : "name.pem",
      "pem_key" : "key2.pem",
      "type" : "t2micro",
      "AMI" : 40,
      "volume" : "30GB" ,
      }

other_details = {
                "security" : "SSH"
}


EC2.update(other_details) # updates EC2 with another dictionary 
print(EC2)

EC2["something"] = 100  #It can add key value pair at last
print(EC2)

del EC2["something"]  #delete key value pair
print(EC2)

EC2.pop("pem_key") # It can only delete with key  
print(EC2)

EC2.popitem() # It is used to delete last key value pair
print(EC2)

EC2.clear() # It clears entire dictionary
print(EC2)








