from functools import reduce
l = [256, 74, 55, 95, 25, 110, 467]

def greatest(a, b):
    if a>b:
        return a
    return b

myList = reduce(greatest, l)
print(myList)