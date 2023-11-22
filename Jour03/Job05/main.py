def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
            return num1 / num2
    elif operator == "%":
            return num1 % num2
    else:
        return "operation invalide"

result = calcule(10, "+", 5)
print(result)

result = calcule(20, "*", 3)
print(result)

result = calcule(15, "/", 3)
print(result)

