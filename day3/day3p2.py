values = {
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5,
    "f":6,
    "g":7,
    "h":8,
    "i":9,
    "j":10,
    "k":11,
    "l":12,
    "m":13,
    "n":14,
    "o":15,
    "p":16,
    "q":17,
    "r":18,
    "s":19,
    "t":20,
    "u":21,
    "v":22,
    "w":23,
    "x":24,
    "y":25,
    "z":26,    
    }

totalScore = 0

def calcScore(char):
    if (char.islower()):
        return values[char]
    else:
        return values[char.lower()] + 26

f = open("input.txt", "r")
bags = f.read().split("\n")

counter = 0
groups = []
tmp = []

for line in bags:
    tmp.append(line)
    counter += 1
    if (counter == 3):
        groups.append(tmp)
        tmp = []
        counter = 0

for group in groups:
    badge = ""
    for char in group[0]:
        if (char in group[1] and char in group[2]):
            badge = char
    totalScore += calcScore(badge)

print(totalScore)