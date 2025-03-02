#Zadanie 137. Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpo-
#wiada na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą.
#Długość każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla
#ciągu 110100 nie jest możliwe

from math import log10

def isPrime(n):
    if n <= 1: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False

    i = 5

    while i*i <= n:
        if n % i == 0: return False
        i += 2
        if n % i == 0: return False
        i += 4

    return True

def ciag(T):
    pom = 1
    num = 0
    for i in range(len(T) - 1, -1, -1):
        num += (T[i] * pom)
        pom *= 10


    def rek(num, start, T):
        if start == len(T):
            return True
        l = int(log10(num) + 1)

        for i in range(1,l):
            n1 = num % (10**i)
            n2 = num // 10 ** (l - i - 1)
            if isPrime(n1) and rek(n2, start + 1, T):
                return True

        return False

    return rek(num,0,T)

print(ciag([1,1,1,0,1,1]))