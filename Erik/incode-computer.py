def runProgam(initialStateList, inputsList):
    currState = initialStateList.copy()
    #programLength = len(initialStateList)
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
