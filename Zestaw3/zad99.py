#Zadanie 99. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
#w poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego
#co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić informacje czy udało
#się znaleźć taki ciąg oraz długość tego ciągu.
from itertools import chain

def solve(T):
    N = len(T)
    if N < 3: return False
    begin = N - 2
    #T[w][k]
    while
    cnt = 2
    k = -1
    for w in range(N - 2, -1, -1):
        if w > 0: k = 0
        else: k += 1

        for x in range()
            n1 = T[x][y]
            nk = T[x + 1][y + 1]
            q = nk / n1 if n1 != 0 else q = None
            if q == None:
                cnt = 0
                continue
            if T[x + 2][y + 2] == nk * q:
                cnt =+ 1

            else:
                maxi = max(cnt, maxi)

        maxi = max(cnt, maxi)
