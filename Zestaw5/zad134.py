#Zadanie 134. ”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
#waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
#naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
#równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.
def primes(num):
    summ = 0
    i = 2
    while num > 1:
        if num % i == 0:
            summ += 1

        while num % i == 0:
            num //= i
        i += 1

    return summ

def waga(T):

    def rek(a, b, c, T, i):

        if i == len(T):
            if a == b == c:
                return True
            else:
                return False

        return rek(a + primes(T[i]), b, c, T, i + 1) or rek(a, b + primes(T[i]), c, T, i + 1) or rek(a, b, c + primes(T[i]), T, i + 1)

    result = rek(0, 0, 0, T, 0)
    print(result)

waga([15,15,15])



