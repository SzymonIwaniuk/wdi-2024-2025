#Zadanie 104. Liczby naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą. Dana jest
#tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która zeruje elementy nie posia-
#dające liczby komplementarnej.
def isPrime(a, b):
    suma = a + b
    if suma <= 1: return False
    elif suma == 2 or suma == 3: return True
    elif suma % 2 == 0 or suma % 3 == 0 : return False

    i = 5

    while i*i <= suma:
        if suma % i == 0: return False
        i += 2
        if suma % i == 0: return False
        i += 4

    return True

def isKomp(T, N, i, j):
    num = T[i][j]

    if i - 1 >= 0 and isPrime(T[i][j],T[i-1][j]):
        return True
    if i + 1 < N and isPrime(T[i][j],T[i+1][j]):
        return True
    if j - 1 >= 0 and isPrime(T[i][j],T[i][j-1]):
        return True
    if j + 1 < N and isPrime(T[i][j],T[i][j+1]):
        return True

    return False

def solve(T):
    N = len(T)

    for i in range(N):
        for j in range(N):
            if not isKomp(T, N, i, j):
                T[i][j] = 0

    return T

T = [
    [5, 7, 3],
    [12, 4, 6],
    [11, 9, 8]
            ]

print(solve(T))