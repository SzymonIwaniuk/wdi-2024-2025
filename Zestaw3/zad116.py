#Zadanie 116. Na szachownicy o wymiarach NxN wypełnionej liczbami naturalnym ¿1 odbywają się wy-
#ścigi wież. Pierwsza wieża startuje z lewego górnego rogu i ma dotrzeć do prawego dolnego rogu szachownicy.
#Pierwsza wieża może wykonywać tylko ruchy w prawo lub w dół szachownicy. Druga wie¿a startuje z prawego
#górnego rogu i ma dotrzeć do lewego dolnego rogu szachownicy. Druga wieża może wykonywać tylko ruchy w
#lewo lub w dół szachownicy. Wygrywa wieża, która dotrze do mety w mniejszej liczbie ruchów. Wieże mogą
#wykonać ruch z jednego pola na drugie tylko wtedy, gdy liczby na obu polach są względnie pierwsze. Proszę
#napisać funkcjˆe, która dla danej tablicy zwraca numer wie¿y, która wygra wyścig lub zero jeżeli wyścig będzie
#nierozstrzygnięty. Można założyć, ¿e podczas wyścigu wieże nie spotkają się na jednym polu


def nwd(a, b):
    while b > 0:
        a, b = b, a%b

    return a

def wyscig(T):
    N = len(T)

    def rek1(i, j, cnt, T, N):
        if i == N - 1 and j == N - 1:
            return cnt

        min_moves = 1e10

        for x in range(i + 1, N):
            if nwd(T[i][j], T[x][j]) == 1:
                result = rek1(x, j, cnt + 1, T, N)
                min_moves = min(min_moves, result)

        for y in range(j + 1, N):
            if nwd(T[i][j], T[i][y]) == 1:
                result = rek1(i, y, cnt + 1, T, N)
                min_moves = min(min_moves, result)

        return min_moves

    def rek2(k, l, cnt, T, N):
        if k == N - 1 and l == 0:
            return cnt

        min_moves = 1e10

        for x in range(k + 1, N):
            if nwd(T[k][l], T[x][l]) == 1:
                result = rek2(x, l, cnt + 1, T, N)
                min_moves = min(min_moves, result)

        for y in range(l - 1, -1, -1):
            if nwd(T[k][l], T[k][y]) == 1:
                result = rek2(k, y, cnt + 1, T, N)
                min_moves = min(min_moves, result)

        return min_moves

    result1 = rek1(0,0, 0 , T, N)
    result2 = rek2(0, N - 1, 0, T, N)

    if result1 < result2:
        return 1
    elif result1 == result2:
        return 0
    else:
        return 2

T = [
    [22, 3, 5, 7, 11],
    [13, 17, 19, 23, 29],
    [31, 37, 41, 43, 47],
    [53, 59, 61, 67, 71],
    [73, 79, 83, 89, 55]
]

print(wyscig(T))