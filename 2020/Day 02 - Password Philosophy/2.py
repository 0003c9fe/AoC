import re
with open('input.txt') as file:
    input = [line.rstrip().replace(':','').replace('-',' ').split() for line in file]

def valid1(lower,upper,letter,string):
    i = 0
    for char in string:
        if char == letter:
            i += 1
    return int(lower) <= i <= int(upper)

validCount = 0
for password in input:
    if valid1(password[0],password[1],password[2],password[3]):
        validCount += 1

print('There are',validCount,'valid passwords of the first kind')

def valid2(first,second,letter,string):
    return (string[int(first)-1] == letter and string[int(second)-1] != letter) or (string[int(first)-1] != letter and string[int(second)-1] == letter)

validCount = 0
for password in input:
    if valid2(password[0],password[1],password[2],password[3]):
        validCount += 1

print('There are',validCount,'valid passwords of the second kind')
