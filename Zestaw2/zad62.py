from math import isqrt

def suma_cyfr(n):
    suma = 0
    while n != 0:
        suma += (n % 10)
        n //= 10
    return suma 


def sito(N):
    T = [True for _ in range (N)]
    T[0] = T[1] = False

    for i in range(2, isqrt(N) + 1):
        if T[i]:
            for j in range(i * i, N, i):
                T[j] = False

    return T
    
print(sito(5))




