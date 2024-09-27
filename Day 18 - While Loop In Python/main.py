i = 0 
while(i<=5):
    print(i)
    i = i+1

print("finally loop executed")


# i = int(input("Enter The Number:"))
# while(i<=30):
#     i = int(input("Enter The Number:"))
#     print(i)
# print("loop is exit")


reverse = 10
while(reverse > 0):             #reverse the count
    print(reverse)
    reverse = reverse-1
else:
    print("loop exit")


i = 1
while i < 6:
  print(i)
  if i == 3:
    break               #break statement
  i += 1
print("break statemnt is executed")


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue           #Continue statement
  print(i)
print("continue statemnet is executed")

