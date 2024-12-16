def calculator():
    num1 = float(input("Enter the first number: "))
    op = input("Enter the operator(+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    if op == "+":
        print(f"Result: {num1 + num2}")
    elif op == "-":
        print(f"Result: {num1 - num2}")
    elif op == "*":
        print(f"Result: {num1 * num2}")
    elif op == "/" and num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Invalid operator")              
calculator()