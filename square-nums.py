def square(n):
    
    result = {}

    for i in range(1, n+1):
        result[i] = i ** 2

    return result

a = int(input("Введите число: "))
res = square(a)

print(res)