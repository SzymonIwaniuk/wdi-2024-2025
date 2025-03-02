#Zadanie 165. Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpo-
#wiada na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory
#o jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
#wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.

def podzbiory(T,k):
    def rek(T,z1,z2,i,k):
        if i == len(T):
            if len(z1) + len(z2) == k and sum(z1) == sum(z2):
                return True
            else: return False

        return  (rek(T,z1+[T[i]],z2,i + 1,k) or
                rek(T,z1,z2+[T[i]],i + 1,k) or
                rek(T,z1,z2,i + 1,k))

    return rek(T,[],[],0,k)

T = [3,1,4,3]
k = 4
print(podzbiory(T,k))