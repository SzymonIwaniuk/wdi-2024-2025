def silnia(n):
    silnia = 1
    
    for i in range(1, n + 1):
        silnia *= i
    return silnia

def zad39(n):

    num = silnia(n)
    counter = 0
    
    while num % 10 == 0:
        num //= 10
        counter += 1

    return counter

print(zad39(10))
        
        
