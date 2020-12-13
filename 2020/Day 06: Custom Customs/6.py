with open('input.txt') as file:
    input = [block.split() for block in file.read().split('\n\n')]

unionCounts = 0
intersectionCounts = 0
for block in input:
    block = list(map(set,block))
    unionCounts += len(set.union(*block))
    intersectionCounts += len(set.intersection(*block))

print('The sum of the united counts is',unionCounts)
print('The sum of the intersected counts is',intersectionCounts)
