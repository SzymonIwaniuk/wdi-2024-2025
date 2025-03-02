from math import log10


def ciag(n):
    lenght = int(log10(n)) + 1

    while n:
        if n % 10 == lenght: return True 
        n //= 10
    return False 

print(ciag(12343177))
