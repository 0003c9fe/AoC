with open('input.txt') as file:
    input = [line.rstrip() for line in file]

def valid(a, b, c):
    return (a + b > c and a + c > b and b + c > a)

possible = 0
for triangle in input:
    sides = list(map(int,triangle.split()))
    if valid(sides[0], sides[1], sides[2]):
        possible += 1

print('Considering rows,',possible,'of the listed triangles are possible')

column1 = []
column2 = []
column3 = []
for triangle in input:
    sides = list(map(int,triangle.split()))
    column1.append(sides[0])
    column2.append(sides[1])
    column3.append(sides[2])

possible = 0
columns = [column1, column2, column3]
for column in columns:
    i = 0
    while i < len(column):
        if valid(column[i], column[i+1], column[i+2]):
            possible += 1
        i += 3

print('Considering columns',possible,'of the listed triangles are possible')
