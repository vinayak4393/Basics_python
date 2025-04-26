# write a function in python which takes list as an input and 
# provide the highest number in the list as an output

def maxNum(lst1):
    Highest_num = lst1[0]
    for num in lst1:
        if num > Highest_num:
            Highest_num = num
    return Highest_num

lst2 = [4398, 4536, 4394, 4393, 4389, 4399] 
out = maxNum(lst2)
print(out)               


# you can use built in function max

def highNum(lst3):
    return max(lst3)

lst4 = [232,465,465,494,6,652]
result = highNum(lst4)
print(result)