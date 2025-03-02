#Zadanie 106. Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
#odpowiada na pytanie, czy w tablicy istnieje wiersz, w którym każda liczba zawiera co najmniej jedną cyfrę
#będącą liczbą pierwszą?


def isPrime(n):
    if n <= 1: return False
    elif n == 2 and n == 3: return True
    elif n % 2 == 0 and n % 3 == 0: return False

    i = 5

    while i*i <= n:
        if n % i == 0: return False
        i += 2
        if n % i == 0: return False
        i += 4
    return True

def czy_zawiera(n):
    while n > 0:
        if isPrime(n%10):
            return True
        n //= 10
    return False

def solve(T):
    N = len(T)
    for i in range(N):
        f2 = True
        for j in range(N):
            if not czy_zawiera(T[i][j]):
                f2 = False
        if f2: return True
    return False
T = [
    [6676,4442,4544],
    [444,666,444],
    [4444,68,66]
                 ]

print(solve(T))

