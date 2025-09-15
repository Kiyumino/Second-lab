def sum_odd_nums(n):
    res = 0
    for i in range(1, n + 1, 2):
        res += i
    return res
n = int(input("Введите число: "))
result = sum_odd_nums(n)
print(f"Сумма нечётных чисел до {n}: {result}")