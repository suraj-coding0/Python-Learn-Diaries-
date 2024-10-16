# In Python, a lambda function is a small anonymous function without a name.
# Syntax:- lambda arguments: expression
# Lambda functions are often used in situations where a small function is required for a short period of time. They are commonly used as arguments to higher-order functions, such as map, filter, and reduce.


# def double(x):
#     return x*2

def appl(fx, value):
    return 6 + fx(value)

double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x, y, z: (x+y+z)/3


print(double(5))
print(cube(5))
print(avg(3,5,8))
print(appl(lambda x: x*x*x, 2))


# Lambda function to calculate the product of two numbers,
# with additional print statement
multi = lambda x, y: print(f'{x} * {y} = {x * y}')
(multi(5,4))