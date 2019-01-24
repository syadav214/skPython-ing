from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())
    print(*xrange(1,n+1),sep='',end='\nThis is the end\n')


"""
Example:>
print(*values, sep=' ', end='\n', file=sys.stdout)
print(value1, value2, value3, sep=' ', end='\n', file=sys.stdout)
"""
