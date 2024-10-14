x = 10 # global variable

def my_function():
  y = 5 # local variable
  print(y)

my_function()
print(x)
#print(y) # this will cause an error because y is a local variable and is not accessible outside of the function


#************ Global keyword *************

x = 10 # global variable

def my_function():
  global x
  x = 5 # this will change the value of the global variable x
  global  y 
  y = 18 # local varible

my_function()
print(x) # prints 5
print(y) # this will cause an error because y is a local variable and is not accessible outside of the function