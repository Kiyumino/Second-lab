import math

while True:

    try:
        x = int(input("Введите число: "))
        if x < 0:
            print("Число не может быть отрицательным")
            continue
        break
    
    except ValueError:
        print("Число должно быть полным")

print(math.factorial(x))