
def operator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        else:
            return "Error! Division by zero."
    else:
        return "Invalid operator."


a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
op = input("Enter operator (+, -, *, /): ")

result = operator(a, b, op)
print("Result:", result)
