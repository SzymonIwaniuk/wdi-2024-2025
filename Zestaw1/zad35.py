from math import log10

def zad35(n):
    if n < 1: return None
    lenght = int(log10(n)) + 1
    uniq = n % 10
    
    while n:
        n //= 10
        if n % 10 == uniq: return False

    return True 

print(zad35(1))
