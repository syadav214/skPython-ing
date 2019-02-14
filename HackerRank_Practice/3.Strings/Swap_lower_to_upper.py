s = 'HackerRank.com presents "Pythonist 2".'
newS = ''
for x in s:
    if x.islower():
        newS += x.upper()
    else:
        newS += x.lower()

print(newS)

