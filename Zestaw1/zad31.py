def zad31(n):
    a1 = 2
    an = 2

    while an <= n:

        if n % a1 == 0: return True
        a1 , an = an , 3 * a1 + 1

    return False


print(zad31(1))
