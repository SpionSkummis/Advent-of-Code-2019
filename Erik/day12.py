import re
#with open("Erik/inputs/input12.txt", "r") as f:
#with open("Erik/inputs/testinput121.txt", "r") as f:
with open("Erik/inputs/testinput122.txt", "r") as f:
    moonList = []
    for line in f:
        xPos = int(re.search("x=(-?[0-9]+)",line).group(1))
        yPos = int(re.search("y=(-?[0-9]+)",line).group(1))
        zPos = int(re.search("z=(-?[0-9]+)",line).group(1))
        moonList.append([[xPos,yPos,zPos],[0,0,0]])

def updateSpeed(moonList):
    for moon1 in moonList:
        moon1X = moon1[0][0]
        moon1Y = moon1[0][1]
        moon1Z = moon1[0][2]
        for moon2 in moonList:
            moon2X = moon2[0][0]
            moon2Y = moon2[0][1]
            moon2Z = moon2[0][2]
            if(moon1X > moon2X):
                moon1[1][0] -= 1
            elif(moon1X < moon2X):
                moon1[1][0] += 1
            if(moon1Y > moon2Y):
                moon1[1][1] -= 1
            elif(moon1Y < moon2Y):
                moon1[1][1] += 1
            if(moon1Z > moon2Z):
                moon1[1][2] -= 1
            elif(moon1Z < moon2Z):
                moon1[1][2] += 1

def updatePosition(moonList):
    for moon in moonList:
        moon[0][0] += moon[1][0]
        moon[0][1] += moon[1][1]
        moon[0][2] += moon[1][2]

def getPotentalEnergy(moon):
    return (abs(moon[0][0]) + abs(moon[0][1]) + abs(moon[0][2]))
def getKineticEnergy(moon):
    return (abs(moon[1][0]) + abs(moon[1][1]) + abs(moon[1][2]))
def getSystemEnergy(moonList):
    energySum = 0
    for moon in moonList:
        energySum += (getPotentalEnergy(moon) * getKineticEnergy(moon))
    return energySum

def makeMoonString(moonList):
    moonStr = ""
    for moon in moonList:
        moonStr += str(moon[0][0]) + str(moon[0][1]) + str(moon[0][2]) +  str(moon[1][0]) +  str(moon[1][1]) +  str(moon[1][2])
    return moonStr

# For part 2
moonList2 = moonList.copy()


#Part 1:
for i in range(0,1000):
    updateSpeed(moonList)
    updatePosition(moonList)

#for moon in moonList:
#    print(moon, getPotentalEnergy(moon), getKineticEnergy(moon))
print(getSystemEnergy(moonList))

#Part 2, unfinished:
"""
repeats = 0
moonSet = set()
moonSet.add(makeMoonString(moonList2))
while(True):
    repeats += 1
    updateSpeed(moonList2)
    updatePosition(moonList2)
    
    if(getSystemEnergy(moonList2) == 0):
        print("Zero system energy")
        tempStr = makeMoonString(moonList2)
        if(tempStr in moonSet):
            break
print(repeats)
"""