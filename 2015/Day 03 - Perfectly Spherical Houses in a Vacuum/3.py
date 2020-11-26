with open('input.txt', 'r') as file:
    input = file.read().replace('\n', '')

def vector(x):
    return {
            '>': (1,0),
            '<': (-1,0),
            '^': (0,1),
            'v': (0,-1)
    }[x]

visitedHouses = {(0,0)}
house = (0,0)
for direction in input:
    house = tuple(map(lambda x, y: x + y, house, vector(direction)))
    visitedHouses.add(house)

print(len(visitedHouses),"houses receive at least one present with just Santa")

visitedHouses = {(0,0)}
humanHouse = (0,0)
roboHouse = (0,0)
i = 0

for direction in input:
    if i % 2 == 0:
        humanHouse = tuple(map(lambda x, y: x + y, humanHouse, vector(direction)))
        visitedHouses.add(humanHouse)
    else:
        roboHouse = tuple(map(lambda x, y: x + y, roboHouse, vector(direction)))
        visitedHouses.add(roboHouse)
    i += 1

print(len(visitedHouses),"houses receive at least one present with Santa and Robo-Santa")
