f = open("input.txt", "r")
line = f.read()

marker = []
for i in range(len(line)):
    if(i > 12):
        duplicate = False
        for char in marker:
            t = 0
            for a in marker:
                if a == char:
                    t+= 1
            if (t >= 2):
                duplicate = True
        if(not duplicate):
            if(line[i] in marker):
                marker.pop(0)
                marker.append(line[i])
            else:
                marker.append(line[i])
                print(i + 1)
                print(marker)
                break
        else:
            marker.pop(0)
            marker.append(line[i])
    else:
        marker.append(line[i])