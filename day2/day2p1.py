rIn = "A"
pIn = "B"
sIn = "C"

rRes = "X"
pRes = "Y"
sRes = "Z"

scLose = 0
scDraw = 3
scWin = 6

scR = 1
scP = 2
scS = 3

totalScore = 0

def check(a, b):
    if (a == "A"):
        if (b == "X"):
            return scDraw
        elif (b == "Y"):
            return scWin
        elif (b == "Z"):
            return scLose

    elif (a == "B"):
        if (b == "X"):
            return scLose
        elif (b == "Y"):
            return scDraw
        elif (b == "Z"):
            return scWin
    
    elif (a == "C"):
        if (b == "X"):
            return scWin
        elif (b == "Y"):
            return scLose
        elif (b == "Z"):
            return scDraw

f = open("input.txt", "r")
rounds = f.read().split("\n")

for round in rounds:
    tmp = []
    roundScore = 0
    for char in round:
        if(char != ' '):
            tmp.extend(char)
        if(char == 'X'):
            roundScore += scR
        elif(char == 'Y'):
            roundScore += scP
        elif(char == 'Z'):
            roundScore += scS
    roundScore += check(tmp[0], tmp[1])
    totalScore += roundScore

print(totalScore)
