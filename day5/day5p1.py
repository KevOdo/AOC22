def move(target, step):    
    crateAmount = int(step[0])
    origin = int(step[1]) - 1
    dest = int(step[2]) - 1
    width = len(target[0])
    height = len(target) -1

    col = []
    blanks = 0

    #check how many empty cells are in the origin column
    for i in range(height):
        if(target[i][origin] == '   '):
            blanks += 1

    #select the targeted crates and clear their cells
    for cell in range(crateAmount + blanks):
        if (target[cell][origin] != '   '):
            col.append(target[cell][origin])
            target[cell][origin] = '   '

    #check how far to go to place selected crates
    depth = 0
    for i in range(height):
        if(target[i][dest] == '   '):
            depth += 1
    
    for i in col:
        if(target[depth-1][dest] != '   '):
            target.insert(0,['   ','   ','   ','   ','   ','   ','   ','   ','   '])
            depth += 1
        target[depth-1][dest] = i
        depth -= 1


f = open("input.txt", "r")
lines = f.read().split("\n")

stack = []
procedure = []
tmp = []

for line in lines:
    if(line != ""):
        tmp.append(line)
    else:
        stack.extend(tmp)
        tmp = []

procedure.extend(tmp)
tmp = []
stack2 = []

for item in stack:
    count = 0
    string = ""
    for char in item:
        if(count != 3):
            string += char
            count += 1
        else:
            tmp.append(string)
            string = ""
            count = 0
    tmp.append(string)
    stack2.append(tmp)
    tmp = []

procedure2 = []
for item in procedure:
    item = item.replace("move ", "")
    item = item.replace(" from ", ",")
    item = item.replace(" to ", ",")
    tmp = item.split(",")
    procedure2.append(tmp)

for p in procedure2:
    move(stack2, p)

print("-")
for i in stack2:
    print(i)
print("-")