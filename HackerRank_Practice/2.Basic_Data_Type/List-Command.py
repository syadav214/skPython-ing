"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
"""
if __name__ == '__main__':
    N = int(input())
    ls =[] 
    for _ in range(N):
        cmdWithVal = input().split(' ')
        cmd = cmdWithVal[0]

        if cmd == 'insert':
            ls.insert(int(cmdWithVal[1]),int(cmdWithVal[2]))
        elif cmd == 'print':
            print(ls)
        elif cmd == 'remove':
            ls.remove(int(cmdWithVal[1]))
        elif cmd == 'append':
            ls.append(int(cmdWithVal[1]))
        elif cmd == 'sort':
            ls.sort()
        elif cmd == 'pop':
            ls.pop()
        elif cmd == 'reverse':
            ls.reverse()
        else:
            print('invalid cmd')
