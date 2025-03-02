#Zadanie 111. Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
#Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
#przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie
#wież. Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi
def summ(T,n,i,j,k,l):
    sum1 = sum2 = 0

    for x in range(n):
        if x != j:
            sum1 += T[i][x]
        if x != i:
            sum1 += T[x][j]
        if x != l:
            sum2 += T[k][x]
        if x != k:
            sum2 += T[x][l]

    if i == k:
        for x in range(n):
            if x != j and x != l:
                sum2 -= T[i][x]
    if j == l:
        for x in range(n):
            if x != i and x != k:
                sum2 -= T[x][j]

    return sum1 + sum2


def wierze(T):
    n = len(T)
    pozycja = None
    maxi = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if (k, l) != (i, j):
                        currsum = summ(T, n, i, j, k, l)
                        if currsum > maxi:
                            maxi = currsum
                            pozycja = (i, j), (k, l)

    return pozycja, maxi

T = [
    [3, 1, 2],
    [4, 5, 6],
    [7, 8, 9]
]

print(wierze(T))