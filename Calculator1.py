def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter an operator (+ - * /): ")

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    else:
        print("Invalid operator")
        print("Choose another operator")
        calculator()

def main():
    calculator()

if __name__ == "__main__":
    main()
