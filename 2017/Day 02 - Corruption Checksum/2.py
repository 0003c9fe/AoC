with open('input.txt') as file:
    input = [list(map(int,line.rstrip().split())) for line in file]

checksum = 0
for row in input:
    checksum += max(row) - min(row)

print('The first checksum for the spreadsheet is',checksum)

checksum = 0
for row in input:
    for i in range(len(row)-1):
        for j in range(i+1,len(row)):
            if (row[i] % row[j] == 0) or (row[j] % row[i] == 0):
                checksum += int(max(row[i] / row[j], row[j] / row[i]))

print('The second checksum for the spreadsheet is',checksum)
