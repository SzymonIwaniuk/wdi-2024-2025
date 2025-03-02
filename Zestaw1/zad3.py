def zad3():
    suma = 1e10
    N = 2024
    for a in range(1, N - 1):
        for b in range(1, N - 1):
            a1 = a
            b1 = b
            counter = a + b
            while a1 < N:
                a1, b1 = b1, a1 + b1
                if a1 == N and counter < suma and a <= b:
                    suma = counter 
                    result_a = a
                    result_b = b
    return result_a, result_b 
print(zad3())
