import re
with open('input.txt') as file:
    input = [line.rstrip() for line in file]

def nice1(string):
    threeVowels = re.search(re.compile(r"[aeiou].*[aeiou].*[aeiou]"),string)
    doubleLetter = re.search(re.compile(r"(.)\1"),string)
    badSubstrings = re.search(re.compile(r"ab|cd|pq|xy"),string)
    return threeVowels and doubleLetter and (not badSubstrings)

niceStrings = 0
for string in input:
    if nice1(string):
        niceStrings += 1

print("There are",niceStrings,"nice strings of the first kind")

def nice2(string):
    doublePair = re.search(re.compile(r"(..).*\1"),string)
    separatedRepetition = re.search(re.compile(r"(.).\1"),string)
    return doublePair and separatedRepetition

niceStrings = 0
for string in input:
    if nice2(string):
        niceStrings += 1

print("There are",niceStrings,"nice strings of the second kind")
