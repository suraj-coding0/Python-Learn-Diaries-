# Python allows the else keyword to be used with the for and while loops too.
# The else block appears after the body of the loop.

for k in []:
    print(k)

else:
    print("sorry no i")


for i in range(6):
    print(i)
    if i == 4:
        break

else:
    print("Sorry no i")


j = 0
while j<7:
    print(j)
    j = j+1
    if j == 4:
        break

else:
    print("Sorry no i")

#  The statements in the else block will be executed after all iterations are completed.The program exits the loop only after the else block is executed.

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")