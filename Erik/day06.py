#with open("Erik/inputs/input06.txt") as f:
#with open("Erik/inputs/testinput061.txt") as f:
with open("Erik/inputs/testinput062.txt") as f:
    inputList = []
    allPlanetsSet = set()
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
print(findOrbitsRec(planetDictionary,"COM",0))
print(findOrbitsRec(planetDictionary,"D",0))


""" Part 2: Make a function that finds the common root of A and B
Modify function 1 to find the steps to certain endpoints
Add the number of steps
Profit"""



def findCommonRoot(plnDict, currentRoot, firstElement, secondElement):
    listOfCurrRoots = []
    currDepth = 0
    for planet in plnDict[currentRoot]:
        if(findCommonRoot(plnDict, planet,firstElement,secondElement)):
            listOfCurrRoots.append(planet)
            return True
        else:
            return False

def findKeyword(plnDict, startPoint, keyword):
    keywordFound = False
    for planet in plnDict[startPoint]:
        print(planet)
        if(planet == keyword):
            return True
        if(planet not in plnDict):
            return False
        if(findKeyword(plnDict,planet,keyword)):
            return True
    return False




print(findKeyword(planetDictionary,"COM","YOU"))
    

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