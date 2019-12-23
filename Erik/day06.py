with open("Erik/inputs/input06.txt") as f:
#with open("Erik/inputs/testinput061.txt") as f:
#with open("Erik/inputs/testinput062.txt") as f:
    inputList = []
    for line in f:
        thisPair = line.strip().split(")")
        inputList.append(thisPair)

def makePlanetDict(planetList):
    """Takes a list in the form of [[planet][planet in orbit],...] and returns a dict {planet:[planets in orbit]}"""
    plnDict = dict()
    for pair in planetList:
        if(pair[0] in plnDict):
            plnDict[pair[0]].append(pair[1])
        else:
            plnDict[pair[0]] = [pair[1]] 
    return plnDict

def findOrbitsRec(plnDict, startPoint, depth):
    """Takes a dict of planets and planets in orbit, the name of the "root" planet and the current number of orbits.
    Returns total number of orbits"""
    thisDepth = depth + 1
    totalOrbits = 0
    if(startPoint not in plnDict):
        return thisDepth -1
    for planet in plnDict[startPoint]:
        #print(thisDepth, planet)
        totalOrbits += findOrbitsRec(plnDict,planet,thisDepth)
    return totalOrbits + depth
    
planetDictionary = makePlanetDict(inputList)
orbitCount = findOrbitsRec(planetDictionary,"COM",0)
print(f"{orbitCount} total orbits!")


# Part 2
def makeChildList(planetList):
    """Takes a list in the form of [[planet][planet in orbit],...] and returns a dict {planet:[planets in orbit]}"""
    plnDict = dict()
    for pair in planetList:
        if(pair[0] in plnDict):
            plnDict[pair[0]].append(pair[1])
        else:
            plnDict[pair[0]] = [pair[1]] 
    return plnDict

def makeParentList(planetList):
    plnDict = dict()
    for pair in planetList:
        if(pair[1] in plnDict):
            plnDict[pair[1]].append(pair[0])
        else:
            plnDict[pair[1]] = pair[0]
    return plnDict

def findKeyword(plnDict, startPoint, keyword):
    #print("Searching",startPoint)
    if(startPoint not in plnDict):
        return False
    for planet in plnDict[startPoint]:
        if(planet == keyword):
            return True
        if(findKeyword(plnDict,planet,keyword)):
            return True
    return False

def solveSteps(childList, parentList, key1, key2, currentSteps):
    currentNode = parentList[key1]
    #print(currentNode, (currentSteps +1))
    steps = currentSteps + 1
    if(findKeyword(childList,currentNode, key2)):
        #print(currentNode, currentSteps)
        return [currentNode, steps]
    return solveSteps(childList, parentList, currentNode, key2, steps)

childList = makeChildList(inputList)
parentList = makeParentList(inputList)
youStep = solveSteps(childList,parentList,"YOU","SAN",0)
sanStep = solveSteps(childList,parentList, "SAN", "YOU",0)

print(f"{(youStep[1] + sanStep[1]) -2} steps required!")
