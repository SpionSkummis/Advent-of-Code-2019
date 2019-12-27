from math import atan2

def parse_input(path_to_input):
    resultList = []
    with open(path_to_input, "r") as f:
        for line in f:
            lineList = []
            for char in line:
                if(char == "#"):
                    lineList.append(1)
                elif(char == "."):
                    lineList.append(0)
            resultList.append(lineList)
    return resultList

def get_relative_position(baseX, baseY, targetX, targetY):
    return (targetX - baseX, targetY - baseY)

def find_visible_asteroids(asteroidMap, xPos, yPos):
    visibleSet = set()
    for y in range(len(asteroidMap)):
        for x in range(len(asteroidMap[0])):
            if((not(x == xPos and y == yPos)) and asteroidMap[y][x]):
                relPos = get_relative_position(xPos, yPos, x, y)
                visibleSet.add(atan2(relPos[0],relPos[1]))
    return len(visibleSet)

def check_all_asteroids(asteroidMap):
    numSet = set()
    for y in range(len(asteroidMap)):
        for x in range(len(asteroidMap[0])):
            if(asteroidMap[y][x]):
                numSet.add(find_visible_asteroids(asteroidMap, x, y))
    return max(numSet)

def run_part_one(case):
    """Runs part one, takes input in form of a string, "main", "test[1-5]"""
    readPath = "Erik/inputs/"
    if(case == "main"):
        readPath += "input10.txt"
    elif(case == "test1"):
        readPath += "testinput101.txt"
    elif(case == "test2"):
        readPath += "testinput102.txt"
    elif(case == "test3"):
        readPath += "testinput103.txt"
    elif(case == "test4"):
        readPath += "testinput104.txt"
    elif(case == "test5"):
        readPath += "testinput105.txt"
    else:
        print("Incorrect input :(")
        return None
    return(check_all_asteroids(parse_input(readPath)))

def find_best_location(asteroidMap, seenAsteroids):
    """Takes a map and the expected maximum asteroids (part1 ans), returns location of base"""
    for y in range(len(asteroidMap)):
        for x in range(len(asteroidMap[0])):
            if(asteroidMap[y][x]):
                if(find_visible_asteroids(asteroidMap, x, y) == seenAsteroids):
                    return (x, y)
    return None

def make_asteroid_dict(asteroidMap, xPos, yPos):
    """Takes a position of a base and a map, and returns a dict Angle:Amount containing the numbers.
    Also inverts the y-axis for the purpose of angle calculations, in order to start lazering in the right direction."""
    angleDict = dict()
    for y in range(len(asteroidMap)):
        for x in range(len(asteroidMap[0])):
            if((not(x == xPos and y == yPos)) and asteroidMap[y][x]):
                relPos = get_relative_position(xPos, yPos, (x), (y))
                currAngle = atan2(relPos[0],(relPos[1] *-1))
                if(currAngle < 0):
                    currAngle = currAngle + 8
                if currAngle in angleDict:
                    angleDict[currAngle].append((get_abs_dist(xPos, yPos, x, y),(x,y)))
                else:
                    angleDict[currAngle] = [(get_abs_dist(xPos, yPos, x, y),(x,y))]
    return angleDict

def get_abs_dist(baseX, baseY, targetX, targetY):
    return abs(targetX - baseX) + abs (targetY - baseY)


def giant_laser(asteroidMap): #, xPos, yPos):
    basePos = find_best_location(asteroidMap, check_all_asteroids(asteroidMap))
    angleDict = make_asteroid_dict(asteroidMap, basePos[0], basePos[1])
    asteroidsDestroyed = 0
    sortedKeyList = sorted(angleDict)

    for key in sortedKeyList:
        angleDict[key] = sorted(angleDict[key])

    while(True):
        for key in sortedKeyList:
            lastRemoved = angleDict[key].pop(0)
            asteroidsDestroyed += 1

            if(asteroidsDestroyed == 200):
                return lastRemoved

        removeKeys = []
        for key in sortedKeyList:
            if(len(angleDict[key]) == 0):
                removeKeys.append(key)
        for key in removeKeys:
            sortedKeyList.remove(key)
        sortedKeyList = sorted(sortedKeyList.copy())

def tiny_calculator(laseranswer):
    return laseranswer[1][0] * 100 + laseranswer[1][1]


mainMap = parse_input("Erik/inputs/input10.txt")
part1ans = check_all_asteroids(mainMap)
print(f"The best location can see {part1ans} asteroids")

part2output = giant_laser(mainMap)
part2ans = tiny_calculator(part2output)
print(f"The 200:th asteroid to be LAZERED is at {part2output[1]}, resulring in the checksum {part2ans}")
