name = ("Suraj")
for i in name:
    print(i)
    if(i=="b"):
        print("this is something special")

# Fruits = ["apple","banana","mango","grapes"]
# for fruit in Fruits:
#     print(fruit)
#     for i in fruit:
#         print(i)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break           #Exit the loop when x is "banana", but this time the break comes before the print
  print(x)

for k in range(5):
    print(k+1)
else:
  print("Finally finished!")        #print a message when the loop has ended

for k in range(3, 20, 3):
    print(k)


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")        #If the loop breaks, the else block is not executed.


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)             #Print each adjective for every fruit


for x in [0, 1, 2]:
  pass                    #not give any output also not give any error


