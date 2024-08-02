"""
n = 3
***
 *
***
"""

"""
n = 4
****
  *
 *
****
"""

n = int(input("Enter the number: "))

for i in range(1, n + 1):
    if i == 1 or i == n:
        print("*" * n, end="")
    else:
        print(" " * (n - i), end="")
        print("*", end="")
        print(" ", end="")
    print("")
