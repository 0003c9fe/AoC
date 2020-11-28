from collections import Counter
with open('input.txt') as file:
    input = [line.rstrip() for line in file]

letters = ['','','','','','','','']
for message in input:
    for i in range(len(message)):
        letters[i] += message[i]

message = ''
for i in range(len(letters)):
    message += Counter(letters[i]).most_common()[0][0]

print("The original error-corrected message is",message)

message = ''
for i in range(len(letters)):
    message += Counter(letters[i]).most_common()[-1][0]

print("The modified error-corrected message is",message)
