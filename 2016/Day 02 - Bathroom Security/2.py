import numpy as np
with open('input.txt') as file:
    input = [line.rstrip() for line in file]

keypadA = np.array([['1','2','3'],['4','5','6'],['7','8','9']])
x, y = 1, 1
code = ''

for instruction in input:
    directions = list(instruction)
    for movement in directions:
        if movement == 'U':
            y -= 1
        elif movement == 'D':
            y += 1
        elif movement == 'L':
            x -= 1
        else:
            x += 1

        if x < 0:
            x = 0
        elif x > 2:
            x = 2
        if y < 0:
            y = 0
        elif y > 2:
            y = 2
    code += keypadA[y][x]

print('The first bathroom code is',code)

keypadB = np.array([['#','#','1','#','#'],['#','2','3','4','#'],['5','6','7','8','9'],['#','A','B','C','#'],['#','#','D','#','#']])
x, y = 2, 2
code = ''

for instruction in input:
    directions = list(instruction)
    for movement in directions:
        oldX = x
        oldY = y
        if movement == 'U':
            y -= 1
        elif movement == 'D':
            y += 1
        elif movement == 'L':
            x -= 1
        else:
            x += 1

        if x < 0:
            x = 0
        elif x > 4:
            x = 4
        if y < 0:
            y = 0
        elif y > 4:
            y = 4

        if keypadB[y][x] == '#':
            x, y = oldX, oldY
    code += keypadB[y][x]

print('The second bathroom code is',code)
