def zad30(k):
    N = 10000
    dx = abs(k - 1) / N
    suma = 0

    for i in range (1, N + 1):
        xi = 1 + (i / N) * abs(k - 1)
        h = 1 / xi
        suma += dx * h

    return suma

print(zad30(7))
