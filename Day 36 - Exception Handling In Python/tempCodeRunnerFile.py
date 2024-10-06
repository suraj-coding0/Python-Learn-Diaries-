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