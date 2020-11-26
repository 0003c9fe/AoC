import numpy as np
with open('input.txt') as file:
    input = [line.rstrip() for line in file]

filteredInput = []
for instruction in input:
    filter1 = instruction.replace('turn ','')
    filter2 = filter1.replace('through ','')
    filter3 = filter2.replace(',',' ')
    filteredInput.append(filter3)

lightGrid = np.zeros((1000,1000), dtype=int)
for instruction in filteredInput:
    splitInstruction = instruction.split()
    operation = splitInstruction[0]
    x1 = int(splitInstruction[1])
    y1 = int(splitInstruction[2])
    x2 = int(splitInstruction[3])
    y2 = int(splitInstruction[4])
    if operation == 'on':
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lightGrid[x][y] = 1
    elif operation == 'off':
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lightGrid[x][y] = 0
    else:
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lightGrid[x][y] = (lightGrid[x][y] + 1) % 2

lightsOn = np.sum(lightGrid, dtype=int)
print("After following the old instructions",lightsOn,"lights are lit")

lightGrid = np.zeros((1000,1000), dtype=int)
for instruction in filteredInput:
    splitInstruction = instruction.split()
    operation = splitInstruction[0]
    x1 = int(splitInstruction[1])
    y1 = int(splitInstruction[2])
    x2 = int(splitInstruction[3])
    y2 = int(splitInstruction[4])
    if operation == 'on':
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lightGrid[x][y] += 1
    elif operation == 'off':
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lightGrid[x][y] = max(0,lightGrid[x][y]-1)
    else:
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                lightGrid[x][y] += 2

brightness = np.sum(lightGrid, dtype=int)
print("After following the new instructions the total brightness is",brightness)
