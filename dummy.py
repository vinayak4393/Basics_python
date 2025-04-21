# Good Morning!!
# Today is a good day!!
# dict1 = { "a" : 10,
#          "b" : 20,
#          }
# print(dict1)

# import sys

# def get_python_version():
#     print("Python Version:", sys.version)
#     print("Version Info:", sys.version_info)

# def sys_module_examples():
#     print("--- Sys Module Examples ---")
#     get_python_version()


# sys_module_examples()





# import sys

# # Function to demonstrate recursion
# def recursive_function(count):
#     if count == 0:
#         return
#     print(count)
#     recursive_function(count - 1)

# # Check the default recursion limit
# print("Default recursion limit:", sys.getrecursionlimit())

# # Set a custom recursion limit
# sys.setrecursionlimit(1500)
# print("New recursion limit:", sys.getrecursionlimit())

# # Call a recursive function with a smaller count
# recursive_function(5)

import re

pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
pattern1 = r"^\d{4}-\d{2}-\d{2}"
pattern2 = r"[6789]\d{9}"
pattern3 = r"(\d{1,3}\.){3}\d{1,3}"

lst1 = [
"2024-25-56",
"2026-59-79",
"7326513265",
"6257485121",
"9215484121",
"2055-46-56tujhjjhihj",
"vghgjygjbu@jkghh.org",
"25.568.23.124",
"564.235.1.12",
"1.2.2.2",
"bv+%hgfjvhfnvkjg@bjhjjh.com"]

for test in lst1:
    if re.match(pattern3, test):
        print(f"'{test}' matches the pattern.")
    else:
        print(f"'{test}' does not match the pattern.")



def exp(n):
    def base(m):
        return m**n
    return base

cube = exp(3)

print(cube(2))

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
    
out = fact(5)
print(out)    


