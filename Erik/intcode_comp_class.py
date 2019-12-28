class IntcodeComputer:
    def __init__(self):
        self.inputPath = "Erik/inputs/"
        self.mainProgramList = []
        self.currentPointer = 0
    
    def parse_input(self, inputFileName):
        """Takes a input file name and parses it to a list, stores it for further use"""
        readFile = self.inputPath + inputFileName
        with open(readFile, "r") as f:
            rawList = f.read().strip().split(",")
            for element in rawList:
                self.mainProgramList.append(int(element))

    def alter_program(self, instruction_position, instruction_value):
        self.mainProgramList[instruction_position] = instruction_value

    def run_program(self):
        while(True):
            if(self.mainProgramList[self.currentPointer] == 1):
                self.mainProgramList[self.mainProgramList[self.currentPointer+3]] = self.mainProgramList[self.mainProgramList[self.currentPointer+1]] + self.mainProgramList[self.mainProgramList[self.currentPointer+2]]
                self.currentPointer += 4
            elif(self.mainProgramList[self.currentPointer] == 2):
                self.mainProgramList[self.mainProgramList[self.currentPointer+3]] = self.mainProgramList[self.mainProgramList[self.currentPointer+1]] * self.mainProgramList[self.mainProgramList[self.currentPointer+2]]
                self.currentPointer += 4
            elif(self.mainProgramList[self.currentPointer] == 99):
                #print("Program finished")
                break
            else:
                print("Unreacable code has been reaced")
                break
#Regulatory and conrol functions below:

                
    def print_maincode(self):
        return self.mainProgramList
