import math
rc = list(map(int, input().split()))
r = rc[0]
c = rc[1]
finalStr = ''
sign = '.|.'
signCnt = 1
center = math.ceil(r/2) - 1
for i in range(r):
    s = ''.join(['-' for l in range(c)])
    if i == center:
        s = s.center(c,'WELCOME')    
    finalStr += s + '\n'
    signCnt += 2
print(finalStr)


"""str = "this is string example....wow!!!"
print(len(str))
print(str.ljust(50, '0'))

str = "this is string example....wow!!!"
print(str.rjust(50, '0'))

str = "this is string example....wow!!!"
print(str.center(50, '0'))
"""
