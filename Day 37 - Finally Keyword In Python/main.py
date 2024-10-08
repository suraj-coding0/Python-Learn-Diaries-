# The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message. 

# Syntax:

# try:
#    #statements which could generate 
#    #exception
# except:
#    #solution of generated exception
# finally:
#     #block of code which is going to 
#     #execute in any situation

# One of the important use cases of finally block is in a function which returns a value.


# Example 1:
def func1():
    try:
        li = [1,2,4,5,7]
        i = int(input("Enter The Number:"))
        print(li[i])
        return 1
    except:
        print("Some Error Occurred")
        return 0

    finally:
        print("I Am Always Executed")

# print("i am always executed")
x = func1()
print(x)

# Example 2:
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
else:
    print("Integer Accepted.")
finally:
    print("This block is always executed.")

