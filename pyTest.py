A = input()
A =  A.split(' ')
x = int(A[0])
y = int(A[1])
z = int(A[2])
n = int(A[3])


for a in range(x+1):
    for b in range(y+1):
        for c in range(z+1):
            #print(a,b,c)
            if a + b + c != n:
                print(a,b,c)
