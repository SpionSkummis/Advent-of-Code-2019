with open("Erik/Day8/input8.txt", "r") as f:
    inputList = list(f.read().strip())

for i in range(0,len(inputList)):
    inputList[i] = int(inputList[i])

def countDigits(layer, digitToFind):
    """A layer is a list of list. The function returns the amount of digitToFind in the layer"""
    mainCounter = 0
    for i in range(0,len(layer)):
        for j in range(0,len(layer[i])):
            if(layer[i][j] == digitToFind):
                mainCounter += 1
    return mainCounter 


allRows = []
for i in range(0,len(inputList),25):
    allRows.append(inputList[i:i+25])

allLayers = []
for i in range(0,len(allRows), 6):
    allLayers.append(allRows[i:i+6])

foundLayer = []
fewestZeroes = 9999999
for i in range(0,len(allLayers)):
    layerAmountOfZero = countDigits(allLayers[i],0)
    if(layerAmountOfZero < fewestZeroes):
        foundLayer = allLayers[i]
        fewestZeroes = layerAmountOfZero

print(countDigits(foundLayer,1)*countDigits(foundLayer,2))

#Part 2
resultLayer = allLayers[0]
for i in range(0,len(allLayers)):
    for j in range(0,len(allLayers[i])):
        for m in range(0,len(allLayers[i][j])):
            if(resultLayer[j][m] == 2):
                resultLayer[j][m] = allLayers[i][j][m]

resultToPicture = ""
for i in range(0,len(resultLayer)):
    for j in range(0,len(resultLayer[i])):
        if(resultLayer[i][j] == 0):
            resultToPicture += " "
        elif(resultLayer[i][j] == 1):
            resultToPicture += "#"
    resultToPicture += "\n"
print(resultToPicture)
