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
                bioSum += (2 ** i)
            i += 1
    return bioSum


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
#Solve part 1:
firstRepeat = findRepeat(deepcopy(inputGrid))
print(f"The biodiversity of the first repeated grid is {firstRepeat[1]} found after {firstRepeat[0]} generations.")


#Part 2:
def checkAdj2(golStack, currentLevel, xPos, yPos):
    adjBugs = 0
    for x in [(xPos -1), (xPos + 1)]:
        if(x > -1 and x < 5): #Get "normal" adj.
            adjBugs += golStack[currentLevel][yPos][x]

    if(xPos == 0): # Get adj from bigger grid:
        adjBugs += golStack[currentLevel+1][2][1]
    elif(xPos == 4):
        adjBugs += golStack[currentLevel+1][2][3]
    elif(yPos == 2 and xPos == 1): #Get adj from smaller grid
        for a in range(0,5):
            adjBugs += golStack[currentLevel-1][a][0]
    elif(yPos == 2 and xPos == 3):
        for a in range(0,5):
            adjBugs += golStack[currentLevel-1][a][4]

    for y in [(yPos -1), (yPos +1)]:
        if(y > -1 and y < 5): #Get "normal" adj.
            adjBugs += golStack[currentLevel][y][xPos]
        
    if(yPos == 0): # Get adj from bigger grid:
        adjBugs += golStack[currentLevel+1][1][2]
    elif(yPos == 4):
        adjBugs += golStack[currentLevel+1][3][2]

    elif(xPos == 2 and yPos == 1): #Get adj from smaller grid
        for a in range(0,5):
            adjBugs += golStack[currentLevel-1][0][a]
    elif(xPos == 2 and yPos == 3):
        for a in range(0,5):
            adjBugs += golStack[currentLevel-1][4][a]
        
    return adjBugs

def getBugsNum(golGrid):
    return sum([sum(line) for line in golGrid])
def getStackBugs(golStack):
    return sum([getBugsNum(grid) for grid in golStack])

def makeGameOfLifeStack(golGrid, stackHeight):
    emptyGrid = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    resultStack = list()
    for a in range(0,stackHeight):
        resultStack.append(deepcopy(emptyGrid))
    resultStack[(stackHeight // 2)] = deepcopy(golGrid)
    return resultStack

def simulateMinute2(golStack):
    """Takes a stack, returns another stack after a simulated minute"""
    newStack = deepcopy(golStack)

    for level in range(1,len(golStack)-1):
        for y in range(len(golStack[0])):
            for x in range(len(golStack[0][0])):
                if(not (x == 2 and y == 2)):
                    adjBugs = checkAdj2(golStack,level,x,y)
                    if(golStack[level][y][x]):
                        if(adjBugs == 1):
                            newStack[level][y][x] = 1
                        else:
                            newStack[level][y][x] = 0
                    else:
                        if(adjBugs == 1 or adjBugs == 2):
                            newStack[level][y][x] = 1
                        else:
                            newStack[level][y][x] = 0
        newStack[level][2][2] = 0

    return newStack

#Solves part 2:
mainStack = makeGameOfLifeStack(inputGrid, 210)
resultStack = deepcopy(mainStack)
for i in range(0,200):
    resultStack = simulateMinute2(resultStack)

part2ans = getStackBugs(resultStack)
print(f"The answer to part two is : {part2ans}")
