from math import sqrt 


def is_prime(n):
    if n <= 1: return False
    elif n == 2 or n == 3: return True
    elif n % 2 == 0 or n % 3 == 0: return False

    i = 5

    while i <= sqrt(n):
        if n % i == 0: return False

        i += 2

        if n % i == 0: return False

        i += 4

    return True

def sys(n, s):
    liczba = 0
    tmp = 1

    while n != 0:
        liczba = liczba + (n % s) * tmp 
        n //= s
        tmp *= 10

    return liczba

def suma(n):
    iloczyn = 1

    while n != 0:
        iloczyn *= n % 10
        n //= 10

    return iloczyn

        
