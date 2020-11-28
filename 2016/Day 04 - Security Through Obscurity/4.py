with open('input.txt') as file:
    input = [line.rstrip() for line in file]

test = input[0]
print(test.replace('-','',test.count('-')-1).split('-'))


#for room in input:
