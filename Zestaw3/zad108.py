#Zadanie 108. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję która
#zwraca wiersz i kolumnę dowolnego elementu, dla którego suma otaczających go elementów jest największa
#T[w][k]
def suma(T, N, i, j):
    b1 = e1 = b2 = e2 = summ = 0
    if i - 1 >= 0: b1 = i - 1
    else: b1 = i
    if i + 1 < N: e1 = i + 1
    else: e1 = i
    if j - 1 >= 0: b2 = i - 1
    else: b2 = j
    if j + 1 < N : e2 = j + 1
    else: e2 = j

    for r in range(b1, e1):
        for c in range(b2, e2):
            summ += T[r][c]

    return summ - T[i][j]

def solve(T):
    N = len(T)
    maxi = summ = x = y = 0
    for i in range(N):
        for j in range(N):
            summ = suma(T, N, i, j)
            if summ > maxi:
                x, y, maxi  = i, j, summ
    return x, y 
T = [
    [2, 3, 4, 5],
    [6, 7, 8, 9],
    [10, 11, 12, 13],
    [14, 15, 16, 17]]

print(solve(T))