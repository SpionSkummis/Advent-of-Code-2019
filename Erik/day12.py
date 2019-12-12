import re
with open("Erik/inputs/input12.txt", "r") as f:
    moonList = []
    for line in f:
        xPos = int(re.search("x=(-?[0-9]+)",line).group(1))
        yPos = int(re.search("y=(-?[0-9]+)",line).group(1))
        zPos = int(re.search("z=(-?[0-9]+)",line).group(1))
        moonList.append([[xPos,yPos,zPos],[0,0,0]])

for moon in moonList:
    print(moon)


