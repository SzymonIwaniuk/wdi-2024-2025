#Zadanie 112. Dana jest plansza o wymiarach NxN zawierająca wartości 0 i 1. Pola o wartości 1 zawierają
#pułapki. Skoczek musi dotrzeć z górnego wiersza planszy do dolnego. Każdy ruch skoczka musi go przybliżać
#do dolnego wiersza. Proszę napisać program, który zwraca długość najkrótszej bezpiecznej drogi skoczka z
#wiersza górnego do wiersza dolnego.

#TODO: BFS przeszukiwanie grafu w szerz

def skoczek(T):
    N = len(T)
    moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]
    squares = [[None for _ in range(N)] for _ in range(N)]

    def rek(i, j, cnt, moves, squares, T, N):

        if i == N - 1 and j == N - 1:
            return cnt

        if T[i][j] == 0:
            squares[i][j] = True
        else:
            squares[i][j] = False

        min_moves = 1e10

        for x, y in moves:
            iprim, jprim = i + x, j + y
            if 0 <= iprim < N and 0 <= jprim < N:
                if squares[iprim][jprim] == None:
                    result = rek(iprim, jprim, cnt + 1 ,moves, squares, T, N)
                    if result != None:
                        min_moves = min(min_moves, result)
                    squares[iprim][jprim]= None

        return min_moves
    result = rek(0, 0, 0, moves, squares, T, N)

    return result

T = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
print(skoczek(T))
