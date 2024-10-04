# Quick Quiz: Write a program to print the fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(3) = f(2) + f(1)
# f(4) = f(3) + f(2)
# f(5) = f(4) + f(3)    #output:- 0, 1, 1, 2, 3, 5, 8, 13, 21 etc.....

def fibonacci (n):
    if(n==0 or n==1):
        return n
    else:
        return(fibonacci(n-1) + (fibonacci (n-2)))

nthvalue = 15

if nthvalue <= 0:
    print("Enter The Posotive Number")
else:
    print("Fibonacci Series")

for i in range(nthvalue):
    print(fibonacci(i))



#Example Of Recursion
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(9)