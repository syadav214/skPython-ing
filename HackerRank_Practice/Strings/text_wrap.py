import textwrap

s = 'ABCDEFGHIJKLMNOQRSTUVWXYZ'
print('***********Using Wrap**************')
print(textwrap.wrap(s,4))

print('***********Using Fill**************')
print(textwrap.fill(s,4))

print('***********Using Loop**************')
newS = ''
for i in range(0,len(s),4):
    newS = newS + s[i:i+4] + '\n'
print(newS)
