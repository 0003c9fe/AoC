# single line to string
with open('input.txt', 'r') as file:
    input = file.read().replace('\n', '')

# multiple lines to list of strings
with open('input.txt') as file:
    input = [line.rstrip() for line in file]
