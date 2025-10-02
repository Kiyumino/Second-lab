num1 = float(input("Первое число: "))
operator = input("Выбери оператор (+, -, *, /): ")
num2 = float(input("Второе число: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Делить на 0 нельзя"
else:
    result = "Неверный оператор"

print(f"Результат: {result}")