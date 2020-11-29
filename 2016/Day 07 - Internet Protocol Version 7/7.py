import re
with open('input.txt') as file:
    input = [line.rstrip() for line in file]

def tls(ip):
    abbaAnywhere = True
    abbaInBrackets = False
    return abbaAnywhere and (not abbaInBrackets)

i = 0
for ip in input:
    if tls(ip):
        i += 1

print(i,"IPs support TLS")
