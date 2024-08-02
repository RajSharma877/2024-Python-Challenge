friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[0])
friends[0] = "Grapes"  # Unlike Strings lists are mutable

print(friends[0])
print(
    friends[1:4]
)  # We can also perform slicing in list to access range of elements from list

# We cannot perform methods on original string python creates new copy of that original string and modify that list
