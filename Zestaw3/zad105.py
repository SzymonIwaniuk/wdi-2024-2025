#Zadanie 105. Dwie liczby naturalne są zgodne jeżeli w zapisie dwójkowym zawierają tę samą liczbę
#jedynek, np. 22 = 10110 i 14 = 1110. Dane są tablice T1[N1][N1] T2[N2][N2], gdzie N2 <= N1. Proszę napisać
#funkcję, która sprawdza czy istnieje takie położenie tablicy T1 wewnątrz tablicy T2, przy którym liczba
#zgodnych elementów jest większa od 33%. Do funkcji należy przekazać tablicę T1 i T2. Obie oryginalne
#tablice powinny pozostać nie zmieniane
#TODO: REMAINDER

def zgodne(a, b):
    cnta = cntb = 0
    while a > 0:
        if a % 2 == 1:
            cnta += 1
        a //= 2

    while b > 0:
        if  b % 2 == 1:
            cntb += 1
        b //= 2

    return cnta == cntb

def solve(T1,T2):
    l_t1 = len(T1)
    l_t2 = len(T2)
    flag = False

    for i in range(l_t1 - l_t2 + 1):
        for j in range(l_t1 - l_t2 + 1):
            cnt = 0
            for w in range(i, l_t2 + i):
                for k in range(j, l_t2 + j):
                    if zgodne(T1[w][k], T2[w - i][k - j]):
                        cnt += 1
            percentage = cnt / (l_t2 * l_t2)
            if percentage > (33/100):

                flag = True

    return flag


T1 = [
    [10,  10, 10,  10,  10],
    [10,  10, 10,  10, 10],
    [10, 10, 10, 10,  10],
    [1,  1, 10, 10, 10],
    [1,  1, 10, 10,  10]
]

# Matrix T2 - 3x3
T2 = [
    [1, 1,  1],
    [ 1, 1, 1],
    [1, 1,  1]
]
print(solve(T1,T2))