def zad28(n):
    eps = 1e10
    f1 = 0
    f2 = 0
    i = 1

    while i*i <= n:
        if n % i == 0:
           factor = n // i

           if abs(factor - i) < eps:
               diff = abs(factor - i)
               f1 = i
               f2 = n // i
        i += 1

    return f1, f2

print( zad28(169412412) )
