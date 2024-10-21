import random
print("welcome to snake, Water, Gun Game ")
def swg():
    Round=1
    playerpoints=0
    computerpoints=0
    while Round<=3:
       
        player=str(input("Enter snake, water or gun :"))
        computer=random.choice(["snake","water","gun"])
        if player==computer:
            print("round is draw")
            playerpoints+=0
            computerpoints+=0
        elif player=="snake" and computer=="water":
            print("Player won the round")
            playerpoints+=1
        elif player=="snake" and computer=="gun":
            print("Computer won the round")
            computerpoints+=1
        elif player=="water" and computer=="snake":
            print("Compute won the round")
            computerpoints+=1
        elif player=="water" and computer=="gun":
            print("Player won the round ")
            playerpoints+=1
        elif player=="gun" and computer=="snake":
            print("Player won the round")
            playerpoints+=1
        elif player=="gun" and computer=="water":
            print("Computer won the round")
            computerpoints+=1
        Round+=1
    if playerpoints>computerpoints:
        print("\nPlayer won the match")
    elif playerpoints<computerpoints:
        print("\nComputer won the match")
    elif computerpoints==playerpoints:
        print("\nMatch is draw")

while True:
    print("\n1. Start the game")
    print("2. Exit the game")
    choice=int(input("Enter your choice : "))
    if choice==1:
        swg()
    if choice==2:
        break