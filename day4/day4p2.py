def check(item):
    num = []
    tmp2 = item.split("-")
    for i in range (int(tmp2[0]), int(tmp2[1]) + 1):
        num.append(i)
    
    return num

def checkOverlap(a,b):
    overlap = False
    for i in a:
        if (i in b):
            overlap = True
    return overlap


totalPairs = 0

f = open("input.txt", "r")
lines = f.read().split("\n")

for line in lines:
    tmp = line.split(",")
    first = check(tmp[0])
    second = check(tmp[1])

    check1 = (item in first for item in second)
    check2 = (item in second for item in first)

    if (checkOverlap(first, second)):
        totalPairs += 1

print(totalPairs)