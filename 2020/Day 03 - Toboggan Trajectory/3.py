with open('input.txt') as file:
    input = [line.rstrip() for line in file]

width = len(input[0])
slopesX = [1,3,5,7,1]
slopesY = [1,1,1,1,2]
answer = 1

for i in range(len(slopesX)):
    x, y = 0, 0
    trees = 0
    slopeX = slopesX[i]
    slopeY = slopesY[i]
    while y < len(input) - 1:
        x = (x + slopeX) % width
        y += slopeY
        if input[y][x] == '#':
            trees += 1
    answer *= trees
    if i == 1:
        part1 = trees

print('Following a slope of right 3 and down 1, you would encounter',part1,'trees')
print('Multiplying the number of trees encountered on each slope gives',answer)
