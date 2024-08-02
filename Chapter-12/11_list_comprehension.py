l = [1, 4, 5, 9, 3, 10]

# squaredlist = []

# for item in l:
#     squaredlist.append(item * item)

# print(squaredlist)

# We can achieve this by using list comprehension
squaredlist = [i*i for i in l]
print(squaredlist)