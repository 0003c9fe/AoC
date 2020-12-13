import string
with open('input.txt', 'r') as file:
    input = [block.split() for block in file.read().split('\n\n')]

def valid(passport):
    length = len(passport)
    cid = any('cid' in key for key in passport)
    return (length == 8) or (length == 7 and not cid)

stage1 = []
for block in input:
    if valid(block):
        stage1.append(block)

print(len(stage1), 'passports are valid by field presence')

rules = {
        'byr': lambda x: 1920 <= int(x) <= 2002,
        'iyr': lambda x: 2010 <= int(x) <= 2020,
        'eyr': lambda x: 2020 <= int(x) <= 2030,
        'hgt': lambda x: (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193) or (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76),
        'hcl': lambda x: x[0] == '#' and len(x) == 7 and all(c in string.hexdigits for c in x),
        'ecl': lambda x: x in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
        'pid': lambda x: len(x) == 9 and x.isnumeric(),
        'cid': lambda x: True
        }

valid = 0
for passport in stage1:
    fields = [field.split(':') for field in passport]
    dictFields = dict(fields)
    if all(rules[key](val) for key, val in dictFields.items()):
        valid +=1

print(valid, 'passports are valid')
