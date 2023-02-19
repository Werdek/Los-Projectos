import random
x, a, roundNum, RoundInd = 0, 0, 0, 1
s = "\n\nROUND OF 16 -"
Winners = list()
barrageTxt = "-----------------------------------------------------------------------------------------------------------"
teams = ["Real Madrid","Paris Saint-Germain","Manchester City","Bayern Munich","Benfica","Porto","Borussia Dortmund", "RB Leipzig", "Eintracht Frankfurt", "Liverpool", "Chelsea", "Tottenham","Napoli","Inter Milan", "AC Milan","Club Brugge"]
teams = random.sample(teams, k=16)
goalRange1 = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,5]
goalRange2 = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3]

while 1+1 == 2:
    roundNum += 1
    if roundNum == 1+a:
        print(s, RoundInd)
        print("\nFirst Leg--------------------------------------------------------------------------------------------------\n")
        num1 = random.choice(goalRange1)
        num2 = random.choice(goalRange2)
        print(teams[0+x], num1,":", num2, teams[1+x])
    elif roundNum == 2+a:
        print("\nSecond Leg-------------------------------------------------------------------------------------------------\n")
        num1_2 = random.choice(goalRange2)
        num2_2 = random.choice(goalRange1)
        print(teams[1+x], num2_2,":", num1_2, teams[0+x],"\n")
        Score1 = num1 + num1_2
        Score2 = num2 + num2_2
        print(barrageTxt)
        print("agg. Score:  ",teams[0+x],Score1,":",Score2,teams[1+x],"\n")
        if Score1 > Score2:
            print(teams[0+x],"advances to the next round!")
            Winner1 = teams[0+x]
        elif Score1 < Score2:
            print(teams[1+x],"advances to the next round!")
            Winner1 = teams[1+x]
        else:
            Winner1 = random.choice([teams[0+x], teams[1+x]])
            print(Winner1, "won by penatly shootout and advances to the next round!")
        RoundInd += 1
        a += 2
        x += 2
        Winners.append(Winner1)
    if len(Winners) == 8:
        s = "\n\nQUARTER FINALS -"
        Winners = random.sample(Winners, k=8)
        teams = Winners
        Winners = []
        RoundInd = 1
        x = 0
    if roundNum == 24:
        s = "\n\nSEMI FINALS -"
        Winners = random.sample(Winners, k=4)
        teams = Winners
        Winners = []
        RoundInd = 1
        x = 0
    if roundNum == 28:
        print("\n\nFINAL\n")
        ScoreF1 = random.choice(goalRange2)
        ScoreF2 = random.choice(goalRange2)
        print(Winners[0], ScoreF1, ":", ScoreF2, Winners[1])
        if ScoreF1 > ScoreF2:
            print("\nAND THE WINNER IS:", Winners[0].upper(),"\n")
        elif ScoreF1 < ScoreF2:
            print("\nAND THE WINNER IS:", Winners[1].upper(),"\n")
        else:
            print("\nAND THE WINNER BY PENALTY SHOOTOUT IS:", random.choice([Winners[0], Winners[1]]).upper(), "\n")
        print(barrageTxt)
        roundNum = 0
        break