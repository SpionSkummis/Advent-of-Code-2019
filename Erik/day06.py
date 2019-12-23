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



""" Part 2: Make a function that finds the common root of A and B
Modify function 1 to find the steps to certain endpoints
Add the number of steps
Profit"""





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

def findCommonRoot(plnDict, startPoint, currDepth, firstElement, secondElement):
    depth = currDepth + 1
    if(startPoint not in plnDict):
        return False
    for planet in plnDict[startPoint]:
        if(findKeyword(plnDict,planet,firstElement) and findKeyword(plnDict,planet,secondElement)):
            findCommonRoot(plnDict, planet, depth, firstElement, secondElement)
            return True, planet
    return False

"""
def cheatRoot(plnDict, startPoint, firstElement, secondElement):
    lowPlan = startPoint
    if(findCommonRoot(plnDict, lowPlan, firstElement, secondElement)):
        lowPlan = findCommonRoot(plnDict, lowPlan, firstElement, secondElement)[1]
        cheatRoot(plnDict, lowPlan, firstElement, secondElement)
    return lowPlan
"""

#def findOrbitsRec(plnDict, startPoint, depth):
#    """Takes a dict of planets and planets in orbit, the name of the "root" planet and the current number of orbits.
#    Returns total number of orbits"""
#    thisDepth = depth + 1
#    totalOrbits = 0
#    if(startPoint not in plnDict):
#        return thisDepth -1
#    for planet in plnDict[startPoint]:
#        #print(thisDepth, planet)
#        totalOrbits += findOrbitsRec(plnDict,planet,thisDepth)
#    return totalOrbits + depth


#print(findKeyword(planetDictionary,"COM","SAN"))
#print(findCommonRoot(planetDictionary,"COM", 0, "YOU","SAN"))
#print(cheatRoot(planetDictionary,"COM","YOU","SAN"))

def findCommonRoot(plnDict, startPoint, depth, firstElement, secondElement):
    """Takes a dict of planets and planets in orbit, the name of the "root" planet and the current number of orbits.
    Returns total number of orbits"""
    thisDepth = depth + 1
    totalOrbits = 0
    if((firstElement) not in fin):
        return thisDepth -1
    for planet in plnDict[startPoint]:
        #print(thisDepth, planet)
        totalOrbits += findOrbitsRec(plnDict,planet,thisDepth)
    return totalOrbits + depth








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


                
childList = makeChildList(inputList)
parentList = makeParentList(inputList)
#print(childList)
#print(parentList)


def solveSteps(childList, parentList, key1, key2, currentSteps):
    currentNode = parentList[key1]
    #print(currentNode, (currentSteps +1))
    steps = currentSteps + 1
    if(findKeyword(childList,currentNode, key2)):
        #print(currentNode, currentSteps)
        return [currentNode, steps]
    return solveSteps(childList, parentList, currentNode, key2, steps)

#print(findKeyword(childList, "D", "SAN"))
#solveSteps(childList, parentList, "YOU", "SAN", 0)
#print(
#print(findKeyword(childList, "D", "SAN"))
youStep = solveSteps(childList,parentList,"YOU","SAN",0)
sanStep = solveSteps(childList,parentList, "SAN", "YOU",0)

print(f"{(youStep[1] + sanStep[1]) -2} steps required!")