# def square(n):
#     return n * n

# The above function can be written by Lambda function. Lambda functions are anonymous functions means a function which has no name.

square = lambda x: x*x
sum = lambda a,b: a+b

print(square(5))
print(sum(67, 89))
