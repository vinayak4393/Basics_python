def multiTable(num):
    
    for z in range(1,11):
        multi = num * z
        print( f"{num} x {z} = {multi}" )
    print()	

inm = int(input("Enter a  number : "))
out = multiTable(inm)
