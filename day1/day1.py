f = open("input.txt", "r")
lines = f.read().split("\n")

tmp = []
highest = 0
pos = 0
pntr = 0

lst = []
for line in lines:
    if(line != ''):
        tmp.append(int(line))
    else:
        print(line)
        elfTotal = sum(tmp)
        lst.extend([elfTotal])
        tmp.clear()

elfTotal = sum(tmp)
lst.extend([elfTotal])
tmp.clear()

s = sorted(lst)
print(s[-1:])
print(sum(s[-3:]))
