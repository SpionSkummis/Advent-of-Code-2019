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
        elif(finalState[i] == 99):
            break
        else:
            print("Unreacable code has been reaced")
    return finalState

#Initial: before running, replace position 1 with the value 12 and replace position 2 with the value 2"
initialState[1] = 12
initialState[2] = 2
day2_ans1 = runProgam(initialState)[0]
print(f"Part 1 answer: {day2_ans1}")

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
day2_ans2 = 100 * noun_final + verb_final
print(f"Part 2 answer: {day2_ans2}")



from intcode_comp_class import IntcodeComputer

day2intcode = IntcodeComputer()
day2intcode.parse_input("input02.txt")
day2intcode.alter_program(1, 12)
day2intcode.alter_program(2, 2)
day2intcode.run_program()

day2_ans1_class = day2intcode.print_maincode()[0] #Part 1

goal = 19690720
n_final = 0
v_final = 0
found = False

for n in range(0,100):
    for v in range(0,100):
        currRun = IntcodeComputer()
        currRun.parse_input("input02.txt")
        currRun.alter_program(1,n)
        currRun.alter_program(2,v) 
        currRun.run_program()
        calcOutput = currRun.print_maincode()[0]
        if(calcOutput == goal):
            n_final = n
            v_final = v
            found = True
            break
    if(found):
        break
day2_ans2_class = 100 * n_final + v_final #Part 2


print(f"Class test. \n Part 1 solution: {day2_ans1_class}, expected: {day2_ans1} \n Part 2 solution: {day2_ans2_class},    expected: {day2_ans2}")
