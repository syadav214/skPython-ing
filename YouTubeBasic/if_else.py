is_male = True
is_tall = False


if is_male or is_tall:
    print('You are a male or tall or both')
else:
    print('You neither male nor tall')

if is_male and is_tall:
    print('You are a male and tall')
elif is_male and not(is_tall):
    print('You are a short')
else:
    print('You are not male or not tall')


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print('Max of 3 is=> '+str(max_num(10, 2, 9)))
