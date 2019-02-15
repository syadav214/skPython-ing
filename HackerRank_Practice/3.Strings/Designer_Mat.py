"""
Designer Mat
    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
"""

import math
rc = list(map(int, input().split()))
r = rc[0]
c = rc[1]
finalStr = ''
sign = '.|.'
signCnt = 1
center = math.ceil(r/2) - 1
negative = False
for i in range(r):
    s = ''.join(['-' for l in range(c)])
    if i == center:
        strToFit = 'WELCOME'
        negative = True
        signCnt -= 2
    else:
        strToFit = ''.join([sign for l in range(signCnt)])
        if negative == False:
            signCnt += 2
        else:
            signCnt -= 2
    l = int((c - len(strToFit))/2)
    s = s[:l] + strToFit + s[l+len(strToFit):]
    finalStr += s + '\n'
print(finalStr)


"""str = "this is string example....wow!!!"
print(len(str))
print(str.ljust(50, '0'))

str = "this is string example....wow!!!"
print(str.rjust(50, '0'))

str = "this is string example....wow!!!"
print(str.center(50, '0'))
"""
