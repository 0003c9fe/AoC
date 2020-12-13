with open('input.txt') as file:
    input = [line.rstrip().split() for line in file]

i = 0
for passphrase in input:
    if len(passphrase) == len(set(passphrase)):
        i += 1

print('There are',i,'valid passphrases')
