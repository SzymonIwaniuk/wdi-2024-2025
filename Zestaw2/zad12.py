from math import log10



def zad12(n):
    lenght = int(log10(n) + 1)
    
    for i in range(1, lenght + 1):
        if n % 10 == lenght:
            return True
        n //= 10
    return False 
        
        
print(zad12(321))
