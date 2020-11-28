import hashlib as hl
input = 'reyedfim'

password = ''
i = 0
while len(password) < 8:
    hashInput = input + str(i)
    if hl.md5(hashInput.encode()).hexdigest()[0:5] == '00000':
        password += hl.md5(hashInput.encode()).hexdigest()[5]
    i += 1

print("The first password is",password)

password = ['_','_','_','_','_','_','_','_']
print()
print('BREAKING PASSWORD ENCRYPTION')
print('============================')
print('          '+''.join(password)+'          ')

i = 0
while '_' in password:
    hashInput = input + str(i)
    hashed = hl.md5(hashInput.encode()).hexdigest()
    if hashed[0:5] == '00000' and ord(hashed[5]) >= 0 and ord(hashed[5]) <= 55:
        if password[int(hashed[5])] == '_':
            password[int(hashed[5])] = hashed[6]
            print('          '+''.join(password)+'          ')
    i += 1
print('============================')
print('  PASSWORD FOUND: '+''.join(password)+'  ')
