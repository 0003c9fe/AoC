with open('input.txt') as file:
    input = [int(line.rstrip()) for line in file]

answer = 0
for i in range(len(input)-1):
    for j in range(i+1,len(input)):
        if input[i] + input[j] == 2020:
            answer = input[i] * input[j]

print('The product of the two entries summing to 2020 is',answer)

answer = 0
for i in range(len(input)-2):
    for j in range(i+1,len(input)-1):
        for k in range(j+1,len(input)):
            if input[i] + input[j] + input[k] == 2020:
                answer = input[i] * input[j] * input[k]

print('The product of the three entires summing to 2020 is',answer)
