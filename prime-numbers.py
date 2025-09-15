def base(n):

    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
    
        if n % i == 0:
            return False
        return True
    
base = [n for n in range(2, 101) if base(n)]

print(base)