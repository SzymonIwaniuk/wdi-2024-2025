#Zadanie 164. Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i zwraca sumę
#iloczynów elementów wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby. Można
#założyć, że liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym etapie funkcja powinna
#wpisać podzielniki do tablicy pomocniczej. Przykład: 60 → [2, 3, 5] → 2+3+5+2∗3+2∗5+3∗5+2∗3∗5 = 71
def factors(num):
    t = []
    i = 2
    while num > 1:
        if num % i == 0:
            t += [i]
            while num % i == 0:
                num //= i
        i += 1
    return t

def suma_podz(num):
    podzielniki = factors(num)
    def rek(i,iloczyn):
        if i == len(podzielniki):
            return iloczyn if iloczyn > 1 else 0
        return rek(i + 1,iloczyn) + rek(i + 1, iloczyn * podzielniki[i])
    return rek(0,1)


print(suma_podz(123))