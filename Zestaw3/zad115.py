#Zadanie 115. Dwie liczby naturalne są ”wspólno-czynnikowe” jeżeli w swoich rozkładach na czynniki
#pierwsze mają dokładnie jeden wspólny czynnik. Na przykład: 24 i 21 albo 32 i 34. Dana jest tablica T [N ][N ]
#zawierająca liczby naturalne. Dwie liczby w tablicy sąsiadują ze sobą wtedy gdy leżą w tym samym wierszu i
#sąsiednich kolumnach albo leżą w tej samej kolumnie i sąsiednich wierszach. Proszę napisać funkcję four(T),
#która zwraca ilość liczb sąsiadujących z 4 liczbami wspólno-czynnikowymi.

def wspolne(a, b):
    flag = 0
    i = 2
    while a > 1 or b > 1:
        if a % i == 0 and b % i == 0:
            flag += 1

        while a % i == 0:
            a //= i

        while b % i == 0:
            b //= i

        i += 1
    if flag == 1: return True
    else: return False

def four(T):
    N = len(T)
    check = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    amt = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for checks in check:
                if 0 <= i + checks[0] < N and 0 <= j + checks[1] < N:
                    if wspolne(T[i][j], T[i + checks[0]][j + checks[1]]):
                        cnt += 1
            if cnt == 4:
                amt += 1
    return amt

T = [
    [24, 21, 76, 89, 12],
    [21, 24, 21, 91, 38],
    [55, 21, 13, 34, 82],
    [78, 31, 34, 32, 34],
    [11, 52, 85, 34, 34]
                        ]

print(four(T))