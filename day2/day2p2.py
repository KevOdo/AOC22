rIn = "A"
pIn = "B"
sIn = "C"

lose = "X"
draw = "Y"
win = "Z"

scLose = 0
scDraw = 3
scWin = 6

scR = 1
scP = 2
scS = 3

totalScore = 0

def choose(a , b):
    tmpScore = 0
    if (b == "X"):
        tmpScore += scLose
        if (a == "A"):
            tmpScore += scS
        elif (a == "B"):
            tmpScore += scR
        elif (a == "C"):
            tmpScore += scP
    elif (b == "Y"):
        tmpScore += scDraw
        if (a == "A"):
            tmpScore += scR
        elif (a == "B"):
            tmpScore += scP
        elif (a == "C"):
            tmpScore += scS
    elif (b == "Z"):
        tmpScore += scWin
        if (a == "A"):
            tmpScore += scP
        elif (a == "B"):
            tmpScore += scS
        elif (a == "C"):
            tmpScore += scR
    return tmpScore

f = open("input.txt", "r")
rounds = f.read().split("\n")

for round in rounds:
    tmp = []
    for char in round:
        if(char != ' '):
            tmp.extend(char)
    totalScore += choose(tmp[0], tmp[1])

print(totalScore)