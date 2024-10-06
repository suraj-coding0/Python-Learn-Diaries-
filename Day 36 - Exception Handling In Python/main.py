# Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.

a = input("Enter The Number:")
print(f"Multiplication table Of {a} is:")

try:
    for i in range (1, 11):
        print(f"{int(a)} x {i} = {int(a)*i}")

# except Exception as err:
#     print(err)

except:
    print ("invalid input")

print("Some Imp Line Of Codes")
print("End Of Program")


# Specific Errors Errors
try:
    num = int(input("Enter The Integer Number:"))
    a = [1,3,5,7,2,4,6,8]
    print(a[num])
except ValueError:
    print("Entered Number Is Not A Integer")
except IndexError:
    print("Index Error")