def zad6(n):
    i = 1
    divisor = 0
    diff = 0
    score = 999999999999999999999999999999999999999999999999999

    while i <= n // 2:
        if n % i == 0:
            divisor = n // i
            diff = divisor - i
            if diff < 0:
                diff = diff - 2 * diff
        if diff < score:
            score = diff
            a = divisor
            b = i
        i += 1
    return a , b



print(zad6(169))
