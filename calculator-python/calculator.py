def calculate(num1, num2, operation):
    if operation == "1":
       return  num1 + num2
    elif operation == "2":
       return  num1 - num2
    elif operation == "3":
       return  num1 * num2
    elif operation == "4":
       return  num1 / num2
    else:
        return "invalid operation"

def main():
    print("Select the operation: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Enter the operation number (1/2/3/4): ")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = calculate(num1, num2, operation)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()