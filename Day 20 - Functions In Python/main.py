# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# In Python a function is defined using the def keyword.
# To call a function, use the function name followed by parenthesis.

def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

# gmean1 = (a*b)/(a+b)
# print(gmean1)
a = 9
b = 8
calculateGmean(a, b)
# gmean2 = (c*d)/(c+d)
# print(gmean2)
c = 8
d = 74
calculateGmean(c, d)



def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass                #The pass statement is used as a placeholder for future code.
  

a = 9
b = 8
# if(a>b):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")
isGreater(a, b)


c = 8
d = 74
# if(c>d):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")
isGreater(c, d)

