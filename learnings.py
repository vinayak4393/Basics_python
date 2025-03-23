my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 
# Get the last 3 elements of the list
portion = my_list[:-1]
print(portion)

lst1 = [1,2,3,4,5]
out = lst1[2]*8
print(out)


# Function to create a list with repeated elements
def create_repeated_list(element, n):
    return [element] * n

# Create a list with '5' repeated 10 times
repeated_list = create_repeated_list(5, 10)

print(repeated_list)

# Convert a string to a list of characters using list comprehension
my_string = "hello"
char_list = [x for x in my_string]

print(char_list)

tpl = (1,2,3,5,6)
out = tpl.index(5)
print(out)



num = [2, 4, 6, 8]
num1 = []
for el in num:
    num1.append(el**2)
    print(num1)

x = 0
while x < 4:
    print("Hi")
    x += 1


def add(x , y):
    total = x + y
    print(f"sum of {x} and {y} is {total}")

add(20,30)   


def create_and_update_dictionary():
    # Create a dictionary with some sample keys and values
    my_dict = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50}
    
    # Iterate over the dictionary and add 5 to each value
    for key in my_dict:
        my_dict[key] += 5
    
    return my_dict

# Call the function and print the updated dictionary

print(create_and_update_dictionary())




def add(x , y):
    total = x + y
    return total

out = add(20,30)
print(out)


num = int(input("Enter multiplication table: "))
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")



num = int(input("Enter number"))
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")













