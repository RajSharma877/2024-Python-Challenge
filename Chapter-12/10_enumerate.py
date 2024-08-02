l = [4, 456, 768, 999, 1345]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

# This can be achieved by using enumerate function

for item, index in enumerate(l):
    print(f"The item number at index {index} is {item}")
