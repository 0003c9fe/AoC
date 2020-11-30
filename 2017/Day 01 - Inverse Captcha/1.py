with open('input.txt', 'r') as file:
    input = file.read().replace('\n', '')

loop = input + input[0]
sum = 0
for i in range(len(loop)-1):
    if loop[i] == loop[i+1]:
        sum += int(loop[i])

print('The solution to the first captcha is',sum)

sum = 0
for i in range(len(input)):
    if input[i] == input[int((i + len(input) / 2)) % len(input)]:
        sum += int(input[i])

print('The solution to the second captcha is',sum)
