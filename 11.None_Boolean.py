# None is often used to check if something is undefined or has no value.

# Boolean ==> True or False
Isitrunning = True
print(Isitrunning) 

"""
Falsy values
==> False, None, 0, 0.0, 0j, '', [], (), {}, set(), range(0)

Truthy values
==> Everything that is not listed above"
"""

isitrunning = True
if isitrunning:
    print("Its a Truthy value")
else:
    print("Its a Falsy value")    

isitrunning = ''
if isitrunning:
    print("Its a Truthy value")
else:
    print("Its a Falsy value")

isitrunning = 0.0
if isitrunning:
    print("Its a Truthy value")
else:
    print("Its a Falsy value")


isitrunning = -100
if isitrunning:
    print("Its a Truthy value")
else:
    print("Its a Falsy value")


isitrunning = 10>20
if isitrunning:
    print("Its a Truthy value")
else:
    print("Its a Falsy value")


isitrunning = set()
if isitrunning:
    print("Its a Truthy value")
else:
    print("Its a Falsy value")


isitrunning = 10==20
if isitrunning:
    print("Its a Truthy value")
else:
    print("Its a Falsy value")




