# Raising Custom errors:-

# In python, we can raise custom errors by using the raise keyword.

a = int(input("Enter any value between 5 and 9:"))
print(a)
if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")


salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")

# In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

# Here's the syntax to define custom exceptions:

# class CustomError(Exception):
#   # code ...
#   pass

# try:
#   # code ...

# except CustomError:
#   # code...