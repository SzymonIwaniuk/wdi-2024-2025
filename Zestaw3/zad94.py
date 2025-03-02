#Zadanie 94. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
#odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
#parzystą.
#T[w][k]
##TODO zredukuj flagi (kwantyfikatory)
def solve(T):
    N = len(T)

    f1 = False #kwantyfikator szczegółowy (istnieje)
    for i in range(N):
        f2 = True #kwantyfikator ogólny  (dla każdego)
        for j in range(N):
            f3 = False #kwantyfikator szczegółowy
            num = T[i][j]
            while num > 0:
                if num % 2 == 0:
                    f3 = True
                num //= 10
            if not f3: f2 = False
        if f2: f1 = True

    return f1

T =    [[23, 85, 34, 55, 12],
        [98, 42, 77, 18, 69],
        [43, 64, 11, 92, 37],
        [49, 88, 61, 15, 25],
        [79, 10, 94, 32, 56]]

print(solve(T))