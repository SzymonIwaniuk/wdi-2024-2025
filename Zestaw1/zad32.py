def zad32(n):
    while n:
        if n % 10 <= n % 100 - 10 * (n % 10):
            return False
        n //= 10
        
    return True 

print(zad32(123456789000000))
