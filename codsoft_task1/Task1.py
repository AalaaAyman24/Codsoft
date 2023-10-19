n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
op = input("Enter the operation (+, -, *, /): ")
result = 0

match op:
    case "+":
        result = n1 + n2
    case "-":
        result = n1 - n2
    case "*":
        result = n1 * n2
    case "/":
        result = n1 / n2
    case _:
        raise ValueError("Invalid operation!")


print("Result:", result)