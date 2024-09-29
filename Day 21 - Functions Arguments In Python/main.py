def average(a, b):
    print("average:", (a+b)/2)

average(4, 5)


# Default arguments are values that are provided while defining functions.
# The assignment operator = is used to assign a default value to the argument.
# If we provide a value to the default arguments during function calls, it overrides the default value.
def add(a,b=5,c=10):            #the default value is given to argument b and c
    return (a+b+c)

print(add(3,4,5))             #Giving Only the Mandatory Argument



# During a function call, values passed through arguments don’t need to be in the order of parameters in the function definition.
def add(a,b=5,c=10):        #All parameters are given as keyword arguments, so there’s no need to maintain the same order.
    return (a+b+c)

print (add(b=10,c=15,a=20))         #Calling the function add by giving keyword arguments


#During a function call, values passed through arguments should be in the order of parameters in the function definition.
# Keyword arguments should follow positional arguments only.
def add(a,b,c):
    return (a+b+c)

print (add(10,20,30))



# Variable-length arguments are also known as arbitrary arguments. If we don’t know the number of arguments needed for the function in advance, we can use arbitrary arguments. 
def add(*b):
    result=0
    for i in b:
         result=result+i
    return result

print (add(1,2,3,4,5))
print (add(10,20))



# For arbitrary keyword argument, a double asterisk (**) is placed before a parameter in a function which can hold keyword variable-length arguments.
def fn(**a):
    for i in a.items():
        print (i)
fn(numbers=5,colors="blue",fruits="apple")