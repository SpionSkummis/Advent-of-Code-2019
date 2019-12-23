with open("Erik/inputs/input02.txt") as f:
    rawList = f.read().strip().split(",")
    initialState = []
    for element in rawList:
        initialState.append(int(element))

#Test cases
case1 = [1,0,0,0,99] #becomes 2,0,0,0,99 (1 + 1 = 2).
case2 = [2,3,0,3,99] #becomes 2,3,0,6,99 (3 * 2 = 6).
case3 = [2,4,4,5,99,0] #becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
case4 = [1,1,1,4,99,5,6,0,99] # becomes 30,1,1,4,2,5,6,0,99    

def runProgam(initialList):
    finalState = initialList.copy()
    for i in range(0, len(initialList),4):
        if(finalState[i] == 1):
            finalState[finalState[i+3]] = finalState[finalState[i+1]] + finalState[finalState[i+2]]
        elif(finalState[i] == 2):
            finalState[finalState[i+3]] = finalState[finalState[i+1]] * finalState[finalState[i+2]]
        elif(finalState[i == 99]):
            break
        else:
            print("Unreacable code has been reaced")
    return finalState

#Initial: before running, replace position 1 with the value 12 and replace position 2 with the value 2"
initialState[1] = 12
initialState[2] = 2
print(f"Part 1 answer: {runProgam(initialState)[0]}")

#Number to reach 19690720.  474000 too high
goal = 19690720
noun_final = 0
verb_final = 0
found = False

for noun in range(0,100):
    for verb in range(0,100):
        initialState[1] = noun
        initialState[2] = verb
        if(runProgam(initialState)[0] == goal):
            #print(runProgam(initialState)[0])
            noun_final = noun
            verb_final = verb
            found = True
            break
    if(found):
        break

#print(noun_final,verb_final)
print(f"Part 2 answer: {100 * noun_final + verb_final}")
