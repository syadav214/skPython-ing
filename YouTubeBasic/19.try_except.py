try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ValueError:
    print("Invalid input")
except ZeroDivisionError as err:  # assign to a variable to read the error
    print(err)
    print("Cannot divide by Zero")
