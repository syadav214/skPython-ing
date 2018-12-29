def simple_calc():
    num1 = float(input("Enter first number:"))
    op = input("Enter first number:")
    num2 = float(input("Enter second number:"))

    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        return num1/num2
    elif op == "*":
        return num1*num2
    else:
        return "Invalid Operator"


print(simple_calc())
