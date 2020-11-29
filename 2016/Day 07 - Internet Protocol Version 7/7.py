import re
with open('input.txt') as file:
    input = [line.rstrip() for line in file]

string1 = 'xxx'
string2 = 'xyx'

aba = re.compile(r"(.)(?!\1)\1")
print(re.search(aba,string2))
