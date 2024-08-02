from functools import reduce

# Map function example: Map applies a function to all the items in an input_list.

l = [1, 2, 44, 65, 78]

square = lambda x: x * x

sqList = map(square, l)
print(list(sqList))

# Filter example: Filter creates a list of items for which the function returns true.


def even(n):
    if n % 2 == 0:
        return True
    return False


onlyEven = filter(even, l)

print(list(onlyEven))

# Reduce example: Reduce provides a sequential computation for two elements in a list.
product = lambda a, b: a * b

prodList = reduce(product, l)
print(prodList)
