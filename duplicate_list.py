# write python function to identify all the duplicate elements in a list

def duplicate(lst1):
    x = set()
    y = []

    for el in lst1:
        if el in x and el not in y:
            y.append(el)
        else:
            x.add(el)
    return y            


lst2 = [10, 20, 50, 80, 30, 50, 80, 70]
out = duplicate(lst2)
print(out)



