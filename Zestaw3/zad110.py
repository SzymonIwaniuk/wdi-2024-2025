#Zadanie 110. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
#zwraca liczbę par elementów, o określonym iloczynie, takich że elementy są odległe o jeden ruch skoczka
#szachowego.


def solve(T, iloczyn):
    N = len(T)
    cnt = 0

    ruchy_skoczka = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
                                        ]
    for i in range(N):
        for j in range(N):
            for dx, dy in ruchy_skoczka:
                ni, nj = i + dy, j + dx

                if 0 <= ni < N and 0 <= nj < N:

                    if T[i][j] * T[ni][nj] == iloczyn:
                        cnt += 1

    return cnt // 2

T = [
    [1, 2, 1],
    [4, 5, 15],
    [1, 15, 9]]

k = 15

print(solve(T,k))