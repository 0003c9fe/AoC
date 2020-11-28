with open('input.txt', 'r') as file:
    input = file.read().replace('\n', '').split()

directions = [x.replace(',','') for x in input]

# 0 is north, increments clockwise
cardinal = 0
def vector(x):
    return {
            0: (0,1),
            1: (1,0),
            2: (0,-1),
            3: (-1,0)
    }[x]

visited = {(0,0)}
location = (0,0)
visitedTwice = []

for direction in directions:
    turn = direction[0]
    length = int(direction[1:])
    if turn == 'R':
        cardinal = (cardinal + 1) % 4
    else:
        cardinal = (cardinal - 1) % 4
    vec = vector(cardinal)
    for i in range(length):
        location = tuple(map(lambda x, y: x + y, location, vec))
        if location in visited:
            visitedTwice.append(location)
        visited.add(location)

taxicab = location[0] + location[1]
firstRepeat = visitedTwice[0]
taxicabRepeat = firstRepeat[0] + firstRepeat[1]
print("The directions lead to a location",taxicab,"blocks away")
print("The first location visited twice is",taxicabRepeat,"blocks away")
