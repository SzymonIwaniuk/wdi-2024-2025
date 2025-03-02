#To samo co 95 tylko tablica z całkowitymi (chodzi o dzielenie przez 0)


def iloraz(T, i, j, N):
    suma1 = suma2 = iloraz = 0
    for k in range(N):
        if k != j:
            suma1 += T[i][k]
        if k != i:
            suma2 += T[k][j]

    iloraz = suma1 / suma2 if suma2 != 0 else 0
    return iloraz

def najwiekszy(T):
    N = len(T)
    index = (0, 0)
    maxi = 0

    for i in range(N):
        for j in range(N):
            wynik = iloraz(T,i,j,N)
            if wynik > maxi:
                maxi = wynik
                index = i, j
    return index

T = T = [[2, 1],
     [1, 2]]


print(najwiekszy(T))