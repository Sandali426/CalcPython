def calculator():
    while True:
        operator = input("Enter an operator (+, -, *, /) or 'exit' to quit: ")

        if operator.lower() == "exit":
            print("Exiting the calculator. Goodbye!")
            break

        try:
            num1 = float(input("Enter the 1st Number: "))
            num2 = float(input("Enter the 2nd Number: "))

            if operator == "+":
                result = num1 + num2
                print(round(result, 3))
            elif operator == "-":
                result = num1 - num2
                print(round(result, 3))
            elif operator == "*":
                result = num1 * num2
                print(round(result, 3))
            elif operator == "/":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(round(result, 3))
            else:
                print(f"{operator} is not a valid operator")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
