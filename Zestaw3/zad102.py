#Zadanie 102. Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory cyfr z których zbudowane są liczby
#są identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N] wypełniona liczbami
#naturalnymi. Proszę napisać funkcję, która dla tablicy T zwraca ile elementów tablicy sąsiaduje wyłącznie z
#przyjaciółkami
def identyczne(a, b):
    d = [False for _ in range(10)]
    while a > 0:
        d[a%10] = True
        a //= 10
    while b > 0:
        if d[b%10] != True:
            return False
        b //= 10
    return True

def bff(T, N, i, j):
    num = T[i][j]
    if i - 1 >= 0:
        if not identyczne(T[i - 1][j], T[i][j]):
            return False
    if i + 1 < N:
        if not identyczne(T[i + 1][j], T[i][j]):
            return False
    if j - 1 >= 0:
        if not identyczne(T[i][j - 1], T[i][j]):
            return False
    if j + 1 < N:
        if not identyczne(T[i][j + 1], T[i][j]):
            return False
    return True
def solve(T):
    N = len(T)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if bff(T, N, i, j):
                cnt += 1
    return cnt

T = [
    [123, 231, 312],
    [231, 321, 123],
    [789, 213, 999]
]
print(solve(T))




