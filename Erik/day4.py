# Input is 147981-691423
inputLow = 147981
inputHigh = 691423
# Det kanske hade varit mer "Python" att skriva inputRange = range(147981,691423)?

def makeList(integer):
    # Only 6-digit integers
    intList = []
    for i in range(6, 0, -1):
        intList.append((integer % (10**i)) // (10**(i-1)))
    return intList

def isValid(inList):
    hasDouble = False
    for i in range(len(inList)-1):
        if(inList[i] > inList[i+1]):
            return False
        if(inList[i] == inList[i+1]):
            hasDouble = True
    if(hasDouble):
        return True
    else:
        return False

def isValidInt(integer):
    inList = makeList(integer)
    hasDouble = False
    for i in range(len(inList)-1):
        if(inList[i] > inList[i+1]):
            return False
        if(inList[i] == inList[i+1]):
            hasDouble = True
    if(hasDouble):
        return True
    else:
        return False
        
def isValidInt2(integer):
    inList = makeList(integer)
    hasSingleDouble = False
    for i in range(len(inList)-1):
        if(inList[i] > inList[i+1]):
            return False
        if(inList[i] == inList[i+1]):
            if((i > 0) and (i < len(inList)-2)):
                if(not((inList[i] == inList[i-1]) or (inList[i] == inList[i+2]))):
                    hasSingleDouble = True
            elif(i == 0):
                if(inList[i] != inList[i+2]):
                    hasSingleDouble = True
            elif(i == len(inList)-2):
                if(inList[i] != inList[i-1]):
                    hasSingleDouble = True
    if(hasSingleDouble):
        return True
    else:
        return False


possiblePasswords = 0
possiblePasswords2 = 0
for pw in range(inputLow, inputHigh):
    if(isValidInt(pw)):
        possiblePasswords += 1
    if(isValidInt2(pw)):
        possiblePasswords2 += 1
print(f"There are {possiblePasswords} possible passwords using the first set of rules")
print(f"There are {possiblePasswords2} possible passwords using the second set of rules")