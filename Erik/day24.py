from copy import deepcopy
with open("Erik/inputs/input24.txt", "r") as f:
#with open("Erik/inputs/testinput241.txt", "r") as f:
    inputGrid = list()
    for line in f:
        tempList = []
        for char in line:
            if(char == "#"):
                tempList.append(1)
            elif(char == "."):
                tempList.append(0)
        inputGrid.append(tempList)

def gridprint(golGrid):
    """Test function, prints a grid"""
    for line in golGrid:
        print(line)

def checkAdj(golGrid, xPos, yPos):
    adjBugs = 0
    for x in range (xPos -1, xPos +2):
        if(x > -1 and x < 5 and x != xPos):
            adjBugs += golGrid[yPos][x]
    for y in range(yPos -1, yPos +2):
        if(y > -1 and y < 5 and y != yPos):
            adjBugs += golGrid[y][xPos]
    return adjBugs

def simulateMinute(golGrid):
    """Takes a grid, returns another grid with a simulated minute"""
    #workGrid = golGrid.deepcopy()
    newGrid = deepcopy(golGrid)
    for y in range(len(golGrid)):
        for x in range(len(golGrid[0])):
            adjBugs = checkAdj(golGrid, x, y)
            if(golGrid[y][x]):
                if(adjBugs == 1):
                    newGrid[y][x] = 1
                else:
                    newGrid[y][x] = 0
            else:
                if(adjBugs == 1 or adjBugs == 2):
                    newGrid[y][x] = 1
                else:
                    newGrid[y][x] = 0
    return newGrid

def calcBiodiversity(golGrid):
    bioSum = 0
    i = 0
    for y in range(len(golGrid)):
        for x in range(len(golGrid[0])):
            if(golGrid[y][x]):
                print(x, y, (2 ** i))
                bioSum += (2 ** i)
            i += 1
    return bioSum

def gridConvert(golGrid):
    """Takes a grid, outputs as string in order to add to sets"""
    pass

def findRepeat(golGrid):
    repeatFound = False
    generations = 0
    currGrid = deepcopy(golGrid)
    seenBioSum = set()
    seenBioSum.add(calcBiodiversity(currGrid))
    while(not repeatFound):
        generations += 1
        currGrid = simulateMinute(currGrid)
        currBioSum = calcBiodiversity(currGrid)
        if(currBioSum in seenBioSum):
            return generations, currBioSum
        else:
            seenBioSum.add(currBioSum)
        


def checkAdj(golGrid, xPos, yPos):
    adjBugs = 0
    for x in range (xPos -1, xPos +2):
        if(x > -1 and x < 5 and x != xPos and x != 2):
            adjBugs += golGrid[yPos][x]
    for y in range(yPos -1, yPos +2):
        if(y > -1 and y < 5 and y != yPos y):
            adjBugs += golGrid[y][xPos]
    return adjBugs


print(findRepeat(inputGrid))