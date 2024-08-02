n = int(input("Enter the number: "))

i = 1
sum = 0

# i = 1
# 1 <= 9 ==> n = 9
# sum = 0 + 1 = 1
# i = 1+1 = 2

while i <= n:
    sum += i
    i += 1

print(sum)
