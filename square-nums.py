def square(n):
    
    result = {}

    for i in range(1, n+1):
        result[i] = i ** 2

    return result

num = int(input("Введите число: "))
result = square(num)

print(result)