#Tuple ordered collection of heterogenous data types 
#    ==>Immutable  ==>Faster to access ==>Read only files ==> uses () braces

tpl1 = ("Linux","Python","AKS")
print(tpl1)
print(tpl1[1])

# tpl1[0] = "JAVA" not possible as immutable

#typecasting is converting list to tuple or vice versa
tpl1 = list(tpl1)
print(tpl1)

tpl1 = tuple(tpl1)
print(tpl1)





