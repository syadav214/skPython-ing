"""
The any function (which is in Python's standard library) 
returns true if a list contains at least one True value.

"(method (c) for c in s)" is a for comprehension. 
It takes each character in the string s in turn and applies to it 
the function stored in "method", returning a sequence of booleans.

"""
if __name__ == '__main__':
    s = 'qA2'
    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
          print(any(method(c) for c in s))
