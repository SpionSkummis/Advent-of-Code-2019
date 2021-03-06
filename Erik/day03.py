with open("Erik/inputs/input03.txt") as f:
    cable1 = f.readline().strip().split(",")
    cable2 = f.readline().strip().split(",")

#Test cases: 
#cable1 = ["R8","U5","L5","D3"]
#cable2 = ["U7","R6","D4","L4"]
#cable1 = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
#cable2 = ["U62","R66","U55","R34","D71","R55","D58","R83"]
#cable1 = ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"]
#cable2 = ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]

def makeVisitedSet(inList):
    firstVisited = set()
    xPos = 0
    yPos = 0
    firstVisited.add((xPos,yPos))
    for instruction in inList:
        direction = instruction[0]
        length = int(instruction[1:])
        if(direction == "U"):
            for i in range(yPos,(yPos+length)):
                firstVisited.add((xPos,i))
            yPos += length
        elif(direction == "D"):
            for i in range(yPos,(yPos-length),-1):
                firstVisited.add((xPos,i))
            yPos -= length
        elif(direction == "R"):
            for i in range(xPos,(xPos+length)):
                firstVisited.add((i,yPos))
            xPos += length
        elif(direction == "L"):
            for i in range(xPos, (xPos-length),-1):
                firstVisited.add((i,yPos))
            xPos -= length
    return firstVisited


visited1 = makeVisitedSet(cable1)
visited2 = makeVisitedSet(cable2)

crossSet = set()
for elem in visited1:
    if(elem in visited2):
        crossSet.add(elem)
crossSet.remove((0,0))

lenList = []
for elem in crossSet:
    x, y = elem
    lenList.append(abs(x) + abs(y))
print(sorted(lenList)[0])


def makeVisitedSet2(inList):
    firstVisited = set()
    xPos = 0
    yPos = 0
    steps = 0
    firstVisited.add(((xPos,yPos),(steps)))
    for instruction in inList:
        direction = instruction[0]
        length = int(instruction[1:])
        if(direction == "U"):
            for i in range(yPos,(yPos+length)):
                firstVisited.add(((xPos,i),(steps)))
                steps += 1
            yPos += length
        elif(direction == "D"):
            for i in range(yPos,(yPos-length),-1):
                firstVisited.add(((xPos,i),(steps)))
                steps += 1
            yPos -= length
        elif(direction == "R"):
            for i in range(xPos,(xPos+length)):
                firstVisited.add(((i,yPos),(steps)))
                steps += 1
            xPos += length
        elif(direction == "L"):
            for i in range(xPos, (xPos-length),-1):
                firstVisited.add(((i,yPos),(steps)))
                steps += 1
            xPos -= length
    return firstVisited


visited21 = makeVisitedSet2(cable1)
visited22 = makeVisitedSet2(cable2)

distSet = set()
for c1elem in visited21:
    if c1elem[0] in crossSet:
        for c2elem in visited22:
            if ((c2elem[0] == c1elem[0]) and (c2elem[0] in crossSet)):
                distSet.add((c1elem,c2elem))


distList = []
for elem in distSet:
    distA = elem[0][1]
    distB = elem[1][1]
    distList.append(distA + distB)
print(sorted(distList)[0])
