def zad7(n):
    i = 1

    while i <= n:
        if n % (i * i + i + 1) == 0:
            return i
        i += 1

    return False

print(zad7(33))
