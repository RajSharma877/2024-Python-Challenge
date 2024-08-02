# For two operands
# class Number:
#     def __init__(self, n):
#         self.n = n

#     def __add__(self, num):
#         return self.n + num.n


# a = Number(1)
# b = Number(2)
# print(a + b)


class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        # Since `other` is the second operand, we add `self.n` and `other.n`
        return Number(self.n + other.n)

    def __repr__(self):
        return str(self.n)


a = Number(1)
b = Number(2)
c = Number(3)

# Add a + b first
result = a + b  # This will be a Number instance with n = 1 + 2 = 3

# Then add result + c
result = result + c  # This will be a Number instance with n = 3 + 3 = 6

print(result)  # Output: 6
