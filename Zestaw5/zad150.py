#Zadanie 150. Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie
#muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
#wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
#75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
#zadanych liczb.
from math import log10, sqrt

def is_prime(n):
    if n <= 1: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False

    i = 5

    while i <= sqrt(n):
        if n % i == 0: return False

        i += 2

        if n % i == 0: return False

        i += 4

    return True

def build(n1,n2):
    l1 = int(log10(n1)) + 1
    l2 = int(log10(n2)) + 1
    t = [0 for _ in range(l1 + l2)]
    num = (n1 * 10 ** l2) + n2
    for d in range(l1 + l2 - 1, - 1, -1):
        t[d] = num % 10
        num //= 10

    def rek(num,t):
        l = len(t)
        if int(log10(num + 1)) + 1 == l:
            if is_prime(num):
                return 1

            else:
                return 0
        cnt = 0

        for i in range(l):
            if t[i] != -1:
                tmp = t[i]
                t[i] = -1
                cnt += rek(num * 10 + tmp,t)
                t[i] = tmp
        return cnt

    result = rek(0,t)
    return result

print(build(123,75))