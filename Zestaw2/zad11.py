from math import *

def zad11(n):
    lenght = int(log10(n) + 1)

    for i in range(1 ,lenght + 1):
        if not n % 10 > ((n // 10) % 10):
            return False
        n //= 10
    return True

print(zad11(12344567))
            
        
