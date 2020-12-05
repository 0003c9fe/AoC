with open('input.txt') as file:
    input = [line.rstrip() for line in file]

def seatID(p):
    return int(p.translate(p.maketrans('FBLR','0101')),2)

seatIDs = set()
for boardingPass in input:
    seatIDs.add(seatID(boardingPass))

print('The highest seat ID on a boarding pass is',max(seatIDs))

allIDs = set()
for i in range(min(seatIDs),max(seatIDs)):
    allIDs.add(i)

mySeat, = allIDs.difference(seatIDs)
print('The ID of my seat is',mySeat)
