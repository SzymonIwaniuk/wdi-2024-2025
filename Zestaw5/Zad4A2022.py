#Zadanie A4, 20.12.2022 Nazwisko Imię, Numer albumu
#Na szachownicy o rozmiarach N × N reprezentowanej przez tablicę T [N ][N ] umieszczono pewną liczbę
#skoczków. Położenie skoczka w tablicy oznaczono liczbą 1, puste pola oznaczono liczbą 0. Część pustych pól
#na szachownicy jest szachowana przez znajdujące się na niej skoczki. Proszę zaproponować funkcję place(T),
#która znajdzie na szachownicy puste pole położone najbliżej środka szachownicy, takie że umieszczenie tam
#skoczka maksymalnie zwiększy liczbę szachowanych pustych pól. Do funkcji przekazujemy tablicę T zawie-
#rającą położenie skoczków. Funkcja powinna zwrócić pole (wiersz, kolumna), na którym należy umieścić
#skoczka. Odległość pomiędzy polami: (w1, k1) i (w2, k2) jest równa max(abs(w1 − w2), abs(k1 − k2))

def place(T):
    N = len(T)
    maxi = -1
    cnt = X = Y = 0
    distance = 1e10
    moves = [(-2,-1),(-2,1),(-1,2),(1,2),(-2,-1),(-2,1),(-1,-2),(1,-2)]
    szachowane_pola = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if T[i][j] != 1:
                T[i][j] = 1
                for w in range(N):
                    for k in range(N):
                        for x,y in moves:
                            if 0 <= w + x < N and 0 <= k + y < N:
                                szachowane_pola[w + x][k + y] = True
                        for value in szachowane_pola:
                            if value:
                                cnt += 1
                        if cnt >= maxi:
                            tmp = max(abs(i - (N-1)//2), abs(j - (N-1)//2))
                            if tmp < distance:
                                distance = tmp
                                X, Y = i, j
                            maxi = cnt
                            cnt = 0
                T[i][j] = 0
    return X, Y

T = [[0,0,0,1,0],
     [0,0,0,0,0],
     [0,0,1,0,1],
     [0,0,0,0,1],
     [0,0,0,0,0]]

print(place(T))