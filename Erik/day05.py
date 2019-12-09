


def makeList(integer):
    intList = []
    for i in range(len(str(integer)), 0, -1):
        intList.append(int((integer % (10**i)) // (10**(i-1))))
    return intList

print(makeList(100121))

def runProgam(initialState):
    currState = initialState.copy()
    #programLength = len(initialState)
    outputList = []
    
    i = 0
    while(True):
        #Read the opcode
        opcodeList = makeList(currState[i])
        if(currState[i] == 1): #Opcode 1, addition
            currState[currState[i+3]] = currState[currState[i+1]] + currState[currState[i+2]]
            i += 4
        elif(currState[i] == 2): #Opcode 2, multiplication
            currState[currState[i+3]] = currState[currState[i+1]] * currState[currState[i+2]]
            i += 4
        elif(currState[i == 99]): #Opcode 99, exit
            break
        else:
            print("Unreacable code has been reaced")
            break
    
    return currState
