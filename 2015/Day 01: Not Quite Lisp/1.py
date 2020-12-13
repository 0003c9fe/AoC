with open('input.txt', 'r') as file:
    input = file.read().replace('\n', '')

floor = 0
position = 1
hitBasement = False
list = []

for instruction in input:
    if instruction == '(':
        floor += 1
    else:
        floor -= 1
    list.append(floor)

print('Santa stops at floor',floor)
print('Santa first reaches the pasement on instruction',list.index(-1)+1)
