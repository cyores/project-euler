
# Assign numbers to letter in the alphabet
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letterValues = {'': 0, ' ': 0}
for i in range(1, 27):
    letterValues[alphabet[i - 1]] = i

# Open the names
data = open('p022_names.txt')
names = data.read().replace('"', '').split(',')
names.sort()

# point calculation
scoreTotal = 0
index = 1
for item in names:
    score = 0
    for letter in item:
        score += letterValues[letter]
    score *= index

    scoreTotal += score
    index += 1

print(scoreTotal)

data.close()

