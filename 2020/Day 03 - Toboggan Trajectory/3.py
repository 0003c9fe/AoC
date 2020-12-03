with open('input.txt') as file:
    input = [line.rstrip() for line in file]

width = len(input[0])
slopeX = 3
slopeY = 1

x, y = 0, 0
trees = 0
while y < len(input) - 1:
    x = (x + slopeX) % width
    y += slopeY
    if input[y][x] == '#':
        trees += 1

print('Following a slope of right 3 and down 1, you would encounter',trees,'trees')

slopesX = [1,3,5,7,1]
slopesY = [1,1,1,1,2]
treeCounts = []

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
    treeCounts.append(trees)

answer = 1
for trees in treeCounts:
    answer *= trees
print('Multiplying the number of trees encountered on each slope gives',answer)
