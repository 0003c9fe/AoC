import hashlib as hl
input = 'iwrupvqb'

found = False
answer = 1
while not found:
    hashInput = input + str(answer)
    found = (hl.md5(hashInput.encode()).hexdigest()[0:5] == '00000')
    answer += 1

print('The lowest positive number producing a hash with 5 leading zeroes is',answer-1)

found = False
answer = 1
while not found:
    hashInput = input + str(answer)
    found = (hl.md5(hashInput.encode()).hexdigest()[0:6] == '000000')
    answer += 1

print('The lowest positive number producing a hash with 6 leading zeroes is',answer-1)
