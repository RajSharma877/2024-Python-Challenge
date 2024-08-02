l = [256, 74, 55, 95, 25, 110, 467]


def divisibleByFive(n):
    if n % 5 == 0:
        return True
    return False


newList = filter(divisibleByFive, l)

print(list(newList))
