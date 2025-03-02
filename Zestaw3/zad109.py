#Zadanie 109. Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. Proszę napisać funkcję, która
#wyszuka spójny podciąg elementów leżący poziomo lub pionowo o największej sumie. Maksymalna długość
#podciągu może wynosić 10 elementów. Do funkcji należy przekazać tablicę T, funkcja powinna zwrócić sumę
#maksymalnego podciągu.


def solve(T):
    N = len(T)
    maxi = 0

    for i in range(N):
        for start in range(N):
            suma = 0
            for length in range(10):
                if start + length >= N:
                    break
                suma += T[i][start + length]
                maxi = max(maxi, suma)

    for j in range(N):
        for start in range(N):
            suma = 0
            for length in range(10):
                if start + length >= N:
                    break
                suma += T[start + length][j]
                maxi = max(maxi, suma)
    return maxi

T = [    [6, -1, -9, 5, -10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [2, 10, 5, 3, -9, 2, 2, -3, 5, 0, -10, 4, 3, 10, 5],
    [-7, -8, -7, -9, -8, -2, -8, -9, 6, -5, -9, -7, 0, 1, 9],
    [3, -5, 7, 0, -3, -9, 7, -2, 3, -5, 7, -5, -7, -9, 2],
    [8, 8, 8, 9, -1, -5, -3, 0, -7, 5, 6, 0, 2, 4, 5],
    [8, -3, -7, 5, 4, 4, 6, 5, 9, 10, -9, -10, -8, 3, -5],
    [-6, 3, 6, 5, -10, -3, 4, 5, 5, -10, 4, 10, 6, 9, -6],
    [1, 10, 9, -9, -5, 7, 0, 1, 5, -1, -1, -6, -4, -9, -1],
    [2, 1, 5, -9, 10, 10, 9, 7, -8, -1, 0, -4, -3, 1, 3],
    [-7, -6, -10, 0, 8, -9, -3, -1, 4, 8, -2, 7, -7, 3, 5],
    [-3, 3, 3, 8, 3, 9, 3, 9, -7, -9, -3, 8, -1, -8, 10],
    [8, 5, 7, -9, 9, 10, -10, 8, -2, 4, 2, -10, 7, 0, 8],
    [-2, -10, 7, -5, -1, -9, -4, 8, 5, -2, -4, -2, -8, 2, 5],
    [10, 7, 3, 9, -2, 1, -3, -8, -5, 9, 5, -5, 9, -4, -5],
    [-2, 3, 7, -9, 2, 4, -1, -10, 2, -6, -6, -1, 5, -3, -5]
                                                            ]
print(solve(T))