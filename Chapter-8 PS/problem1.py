def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else:
        return 0


a = 23
b = 4
c = 66

print(greatest(a, b, c))
