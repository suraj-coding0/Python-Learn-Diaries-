for i in range(11):
    print("2 X", i, "=", 2 * i)
    if(i == 5):
        break
print("Loop Break")


for i in range(6):
    if(i == 3):
       print("skip the iteration")
       continue
    print("2 X", i, "=", 3 * i)

  
i = 0
while True:
  print(i)
  i = i + 1
  if(i%30 == 0):
    break