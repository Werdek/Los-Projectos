import random

a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 = "-"
Grid = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
WhichPlayer = "Player 1"
GridValue = "X"
AIon = False
AIoff = True

def GameEnd():
    if Grid[0] == Grid[1] and Grid[1] == Grid[2] and Grid[2] != "-" and Grid[2] != "O" or Grid[3] == Grid[4] and Grid[4] == Grid[5] and Grid[5] != "-" and Grid[5] != "O" or Grid[6] == Grid[7] and Grid[7] == Grid[8] and Grid[8] != "-" and Grid[8] != "O" or Grid[0] == Grid[4] and Grid[4] == Grid[8] and Grid[8] != "-" and Grid[8] != "O" or Grid[2] == Grid[4] and Grid[4] == Grid[6] and Grid[6] != "-" and Grid[6] != "O" or Grid[0] == Grid[3] and Grid[3] == Grid[6] and Grid[6] != "-" and Grid[6] != "O" or  Grid[1] == Grid[4] and Grid[4] == Grid[7] and Grid[7] != "-" and Grid[7] != "O" or Grid[2] == Grid[5] and Grid[5] == Grid[8] and Grid[8] != "-" and Grid[8] != "O":
        print("Player1 won!")
        quit()
    if Grid[0] == Grid[1] and Grid[1] == Grid[2] and Grid[2] != "-" and Grid[2] != "X" or Grid[3] == Grid[4] and Grid[4] == Grid[5] and Grid[5] != "-" and Grid[5] != "X" or Grid[6] == Grid[7] and Grid[7] == Grid[8] and Grid[8] != "-" and Grid[8] != "X" or Grid[0] == Grid[4] and Grid[4] == Grid[8] and Grid[8] != "-" and Grid[8] != "X" or Grid[2] == Grid[4] and Grid[4] == Grid[6] and Grid[6] != "-" and Grid[6] != "X" or Grid[0] == Grid[3] and Grid[3] == Grid[6] and Grid[6] != "-" and Grid[6] != "X" or  Grid[1] == Grid[4] and Grid[4] == Grid[7] and Grid[7] != "-" and Grid[7] != "X" or Grid[2] == Grid[5] and Grid[5] == Grid[8] and Grid[8] != "-" and Grid[8] != "X":
        print("Player2 won!")
        quit()
    if  Grid[0] != "-" and Grid[1] != "-" and Grid[2] != "-" and Grid[3] != "-" and Grid[4] != "-" and Grid[5] != "-" and Grid[6] != "-" and Grid[7] != "-" and Grid[8] != "-":
        print("It's a draw")
        quit() 

while 1+1 == 2:
    try: 
        LaQuestion = int(input("[1] Play against AI\n[2] Play against friend\n\nEnter here: "))
    except: 
        continue
    if LaQuestion == 1:
        AIon = True
        AIoff = False
        break
    elif LaQuestion != 2:
        print("\nChoose either option 1 or 2 by typing '1' or '2'.")
        break
    break

print("\nChoose a number between 1-9 to place a mark on the grid.")
print("1 2 3\n4 5 6\n7 8 9\n")
print(Grid[0], Grid[1], Grid[2],"\n" + Grid[3], Grid[4], Grid[5], "\n" + Grid[6], Grid[7], Grid[8],"\n")


while AIoff:
    try:
        UserInput = int(input(WhichPlayer + ": "))
    except:
        print("\nType in a number 1-9 which hasn't been used.\n")
        continue

    if  UserInput > 9 or UserInput < 1 or Grid[UserInput-1] != "-":
        print("\nType in a number 1-9 which hasn't been used.\n")
        continue

    if WhichPlayer == "Player 1": WhichPlayer = WhichPlayer.replace("1","2")
    else: WhichPlayer = WhichPlayer.replace("2","1")
    
    for i in range(len(Grid)):
        if Grid[i] == "-" and UserInput == i+1:
            Grid[i] = GridValue
    if GridValue == "X":
        GridValue = "O"
    else: GridValue = "X"
    print(Grid[0], Grid[1], Grid[2],"\n" + Grid[3], Grid[4], Grid[5], "\n" + Grid[6], Grid[7], Grid[8],"\n")

    GameEnd()

##############################################################################################################################################
WhichPlayer = "You"
while AIon:
    if WhichPlayer == "AI":
        GridValue = "O"
        AIChoice = random.choice([1,2,3,4,5,6,7,8,9])
        if Grid[AIChoice-1] != "-": continue
        for x in range(len(Grid)):
            if Grid[x] == "-" and AIChoice == x+1:
                Grid[x] = GridValue
        print("AI:", AIChoice)
        print(Grid[0], Grid[1], Grid[2],"\n" + Grid[3], Grid[4], Grid[5], "\n" + Grid[6], Grid[7], Grid[8],"\n")
        WhichPlayer = WhichPlayer.replace("AI","You")

    try: 
        UserInput = int(input(WhichPlayer + ": "))
    except: 
        print("\nType in a number 1-9 which hasn't been used.\n")
        continue

    if  UserInput > 9 or UserInput < 1 or Grid[UserInput-1] != "-":
            print("\nType in a number 1-9 which hasn't been used.\n")
            continue
    if WhichPlayer == "You": WhichPlayer = WhichPlayer.replace("You","AI")
    
    GridValue = "X"
    for y in range(len(Grid)):
        if Grid[y] == "-" and UserInput == y+1:
            Grid[y] = GridValue

    print(Grid[0], Grid[1], Grid[2],"\n" + Grid[3], Grid[4], Grid[5], "\n" + Grid[6], Grid[7], Grid[8],"\n")

    GameEnd()