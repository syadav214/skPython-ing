"""
#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""

size = 5
# 97 is ascii value of small letter 'a'; it will start from end
start = 97 + size - 1
result = []
maxlen = 0
# loop till top half the Rangoli
for i in range(size):
    if i > 0:
        strVal = ''
        newstr = ''
        end = start - (i+1)
        # create string from last to first character
        for asV in range(start, end, -1):
            strVal += chr(asV)+'-'

        # create string in reverse order
        # start from back excluding 3 chars; to get 'Zero'th index we are subtracting 4
        for j in range(len(strVal)-4, -1, -1):
            newstr += strVal[j]
        strVal += newstr
        if size - 1 == i:
            maxlen = len(strVal)
        result.append(strVal)
    else:
        result.append(chr(start)) # only last character of the rangoli

signUnScore = ''.join(['-' for i in range(maxlen)])

# row can be determine by below formula
r = ((size - 1) * 2) + 1
index = 0
increment = True
for i in range(r):
    resultEle = result[index]
    lenResultEle = len(resultEle)
    startEle = int((maxlen - lenResultEle) / 2)

    # Slice 'string of -' with proper indexes
    print(signUnScore[:startEle] + resultEle +
          signUnScore[(startEle + lenResultEle):])

    # We reach mid of the loop then start decrementing
    if(i == (size - 1)):
        increment = False

    if increment == False:
        index -= 1
    else:
        index += 1
