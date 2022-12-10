def check(item):
    num = []
    tmp2 = item.split("-")
    for i in range (int(tmp2[0]), int(tmp2[1]) + 1):
        num.append(i)
    
    return num

totalPairs = 0

f = open("input.txt", "r")
lines = f.read().split("\n")

for line in lines:
    tmp = line.split(",")
    first = check(tmp[0])
    second = check(tmp[1])

    check1 = all(item in first for item in second)
    check2 = all(item in second for item in first)

    if (check1 or check2):
        totalPairs += 1

print(totalPairs)