import re, numpy
from copy import deepcopy
with open("Erik/inputs/input12.txt", "r") as f:
#with open("Erik/inputs/testinput121.txt", "r") as f:
#with open("Erik/inputs/testinput122.txt", "r") as f:
    moonList = []
    xList = []
    yList = []
    zList = []
    for line in f:
        xPos = int(re.search("x=(-?[0-9]+)",line).group(1))
        yPos = int(re.search("y=(-?[0-9]+)",line).group(1))
        zPos = int(re.search("z=(-?[0-9]+)",line).group(1))
        moonList.append([[xPos,yPos,zPos],[0,0,0]])
        xList.append([xPos,0])
        yList.append([yPos,0])
        zList.append([zPos,0])

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

def makeMoonTuple(moonList):
    moonTup = tuple()
    for moon in moonList:
        tempTup = (moon[0][0], moon[0][1], moon[0][2], moon[1][0], moon[1][1], moon[1][2])
        moonTup += tempTup
    return moonTup

#Part 1:
part1MoonList = deepcopy(moonList)
for i in range(0,1000):
    updateSpeed(part1MoonList)
    updatePosition(part1MoonList)
totalSystemEnergy = getSystemEnergy(part1MoonList)
print(f"The total system energy is {totalSystemEnergy}")

#Part 2, unfinished:

def updatePlaneSpeed(planeList):
    for moon1 in planeList:
        moon1Pos = moon1[0]
        for moon2 in planeList:
            moon2Pos = moon2[0]
            if(moon1Pos > moon2Pos):
                moon1[1] -= 1
            elif(moon1Pos < moon2Pos):
                moon1[1] += 1
    return planeList

def updatePlanePosition(planeList):
    for moon in planeList:
        moon[0] += moon[1]
    return planeList

def makePlaneTup(planeList):
    resTup = tuple()
    for planet in planeList:
        resTup += tuple(planet)
    return resTup


def findPlaneRepeats(inputList):
    planeList = inputList.copy()
    repeats = 0
    seenSet = set()
    planeTup = makePlaneTup(planeList)
    seenSet.add(planeTup)
    while(True):
        updatePlaneSpeed(planeList)
        updatePlanePosition(planeList)
        repeats += 1
        planeTup = makePlaneTup(planeList)
        if(planeTup in seenSet):
            return planeTup, repeats
        seenSet.add(planeTup)

def findFirstState(inputList, keyTuple):
    planeList = inputList.copy()
    print(keyTuple)
    repeats = 0
    planeTup = makePlaneTup(planeList)
    if(planeTup == keyTuple):
        print(planeTup,keyTuple,repeats)
        return repeats
    while(True):
        updatePlaneSpeed(planeList)
        updatePlanePosition(planeList)
        repeats += 1
        planeTup = makePlaneTup(planeList)
        if(planeTup == keyTuple):
            return repeats
    
def findAllRepeats(xPosList, yPosList, zPosList):
    allRepeats = []
    allRepeats.append(findPlaneRepeats(deepcopy(xPosList)))
    allRepeats.append(findPlaneRepeats(deepcopy(yPosList)))
    allRepeats.append(findPlaneRepeats(deepcopy(zPosList)))
    return allRepeats

allRepeats = findAllRepeats(xList, yList, zList)
repList = [allRepeats[0][1], allRepeats[1][1], allRepeats[2][1]]
for element in allRepeats:
    print(element)
part2ans = numpy.lcm.reduce(repList) #Går att skriva om utan numpy med gcd-funktionen ur math, om man är sugen på det
print(f"The system returns to a previously visited state after {part2ans} repeats")
