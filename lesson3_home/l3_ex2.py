try:
    num1 = int(input('Number 1: '))
    num2 = int(input('Number 2: '))
    operator = input('Operator (+, -, *, /, %, **, //): ')

    if operator == "+":
        print("The result is:", num1 + num2)
    elif operator == "-":
        print("The result is:", num1 - num2)
    elif operator == "*":
        print("The result is:", num1 * num2)
    elif operator == "**":
        print("The result is:", num1 ** num2)
    elif operator == "/":
        print("The result is:", num1 / num2)
    elif operator == "%":
        print("The result is:", num1 % num2)
    elif operator == "//":
        print("The result is:", num1 // num2)
except ValueError:
    print("Please enter only numbers!")
except ZeroDivisionError:
    print("Division by zero!")
