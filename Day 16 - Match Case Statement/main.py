#simple match case statement
def runMatch():
   num = int(input("Enter a number between 1 and 3: ")) 
   # match case
   match num:
       # pattern 1
       case 1:
           print("One")
       # pattern 2
       case 2:
           print("Two")
       # pattern 3
       case 3:
           print("Three")
       # default pattern
       case _:
           print("Number not between 1 and 3")
runMatch()



# python match case with if condition
def runMatch():
    num = int(input("Enter a number: "))
    
    # match case
    match num:
        # pattern 1
        case num if num > 0:
            print("Positive")
        # pattern 2
        case num if num < 0:
            print("Negative")
        # default pattern
        case _:
            print("Zero")
            
runMatch()


# # python match case with OR operator
# def runMatch():
#     num = int(input("Enter a number between 1 and 6: "))
    
#     # match case
#     match num:
#         # pattern 1
#         case 1 | 2:
#             print("One or Two")
#         # pattern 2
#         case 3 | 4:
#             print("Three or Four")
#         # pattern 3
#         case 5 | 6:
#             print("Five or Six")
#         # default pattern
#         case _:
#             print("Number not between 1 and 6")
            
# runMatch()


def runMatch():
        Num = int(input("Enter a number B/W 1 To 7: "))

        match Num:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")
            case other:
                print("Invalid")
runMatch()   
        
        
'''

Num = int(input('Enter your number: '))

if (Num == 1):
    print("Monday")
elif (Num == 2):
    print("Tuesday")
elif (Num == 3):
    print("Wednesday")
elif (Num == 4):
    print("Thursday")
elif (Num == 5):
    print("Friday")
elif (Num == 6):
    print("Saturday")
elif (Num == 7):
    print("Sunday")
else: 
    print("invalid number:")

print("happy")

'''  