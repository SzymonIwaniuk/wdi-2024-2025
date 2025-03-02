#Zadanie 133. Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
#co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
#cyfry.

from math import log10

def isPrime(n):
    if n <= 1: return False
    elif n == 2 or n == 3: return True
    elif n % 2 == 0 or n % 3 == 0: return False

    i = 5

    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4

    return True


def rek(num):
    l = int(log10(num)) + 1
    if l >= 2:
        if isPrime(num):
            print(num)
    else:
        return

    tab = [0 for _ in range(l)]

    temp = num
    for j in range(l - 1, - 1, -1):
        tab[j] = temp % 10
        temp //= 10

    for i in range(l):
        new_num = 0
        pom = 1
        for k in range(l - 1, -1, -1):
            if k != i:
                new_num += tab[k] * pom
                pom *= 10
        rek(new_num)

rek(48021)





