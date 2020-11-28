from collections import Counter
with open('input.txt') as file:
    input = [line.rstrip() for line in file]

def checkSum(letters):
    freq = Counter(letters).most_common(5)
    checksum = ''
    for pair in freq:
        checksum += pair[0]
    return checksum

idSum = 0
realRooms = []
for room in input:
    filtered = room.replace('-','',room.count('-')-1).replace('[','-[').split('-')
    letters = sorted(filtered[0])
    sectorID = int(filtered[1])
    checksum = filtered[2].strip('[]')

    if checkSum(letters) == checksum:
        idSum += sectorID
        realRooms.append(room)

print("The sum of the sector IDs of the real rooms is",idSum)
print(realRooms)
