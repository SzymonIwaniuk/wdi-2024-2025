def silnia(n):
    silnia = 1
    
    for i in range(1, n + 1):
        silnia *= i
    return silnia

def zad39(n):

    num = silnia(n)
    
    while num % 10 == 0:
        num //= 10

    num %= 10

    return num

print(zad39(10000))
        
        


