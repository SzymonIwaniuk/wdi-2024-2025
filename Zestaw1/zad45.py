from math import sqrt

def zad45(m, n):
    suma = 0
    sqrtm = sqrt(m)

    while sqrtm > 1:
        sqrtm /= 10

    sqrtm = (sqrtm * 10 ** n) // 1
    
    while sqrtm:
        suma += (sqrtm % 10)
        sqrtm //= 10

    return int(suma)

print(zad45(2, 5))
