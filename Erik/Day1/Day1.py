with open("Erik/Day1/input1.txt") as f:
    partsList = []
    for line in f:
        partsList.append(int(line.strip()))


def fuelCalc(weight):
    return (weight // 3) - 2

def recFuelCalc(weight):
    addedFuel = fuelCalc(weight)
    totalFuel = addedFuel
    while(addedFuel > 8):
        addedFuel = fuelCalc(addedFuel)
        totalFuel += addedFuel
    return totalFuel



fuelSum = 0
fuelSum2 = 0
for part in partsList:
    fuelSum += fuelCalc(part)
    fuelSum2 += recFuelCalc(part)
print(f"First case fuel is {fuelSum} units of fuel")
print(f"Second case fuel is {fuelSum2} units of fuel")
