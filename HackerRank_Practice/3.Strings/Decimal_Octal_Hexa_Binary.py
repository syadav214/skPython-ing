number = 17
width = len("{0:b}".format(number))
for i in range(1, number+1):
    # Print Decimal Octal Hexadecimal Binary
    # print("{0:d} {0:o} {0:X} {0:b}".format(i))

    # Print with proper alignment od width od binary number
    print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))

"""
Decimal = 0 to 9 to form number
Octal = 0 to 7 to form number
Hexadecimal = 16 symbols (base 16). Ten symbols: 0,1,2,3,4,5,6,7,8,9 and includes six extra symbols, i.e. A, B, C, D, E and F. Hexadecimal A = decimal 10, and hexadecimal F = decimal 15. 
Binary = base-2 : typically "0" (zero) and "1" (one). 
"""
