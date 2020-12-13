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
        realRooms.append((' '.join(room.split('-')[0:-1]),sectorID))

print('The sum of the sector IDs of the real rooms is',idSum)

realNames = []
offset = ord('a')
#('amjmpdsj cee qcptgacq', 236)
for room in realRooms:
    words = room[0]
    id = room[1]
    translation = ''
    for letter in words:
        if letter == ' ':
            translation += ' '
        else:
            translation += chr((((ord(letter)-offset)+id) % 26)+offset)
    realNames.append((translation,id))

found = False
i = -1
while not found:
    i += 1
    found = realNames[i][0] == 'northpole object storage'

poleID = realNames[i][1]
print('The sector ID of the room where North Pole objects are stored is',poleID)
