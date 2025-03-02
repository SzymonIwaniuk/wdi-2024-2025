from math import log10

def zad47(suma):
    lenght = int(log10(suma)) + 1

    for n in range(10 ** (lenght - 2), 10 ** (lenght)):
        temp = n
        suma_prim = 0

        while temp:
            suma_prim += temp
            temp //= 10

        if suma == suma_prim:
            return n

    return -1

print(zad47(1333))
        
