#Zadanie 100. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
#w poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
#narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje
#czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.

def solve(T, k):
    N = len(T)
    if N < 3: return False
    elif N % 2 == 0:
        pom = N - 1
    else:
        pom = N

    lenght = 3

    while lenght <= pom:
        for i in range(pom + 1 - lenght):
            for j in range(pom + 1 - lenght):
                pg = T[i][j]
                lg = T[i][j + lenght - 1]
                pd = T[i + lenght - 1][j]
                ld = T[i + lenght - 1][j + lenght - 1]

                if k == pg * lg * pd * ld:
                    srodek_x = i + lenght // 2
                    srodek_y = j + lenght // 2
                    return (srodek_x, srodek_y)

        lenght += 2
    return False

T = [
    [2, 3, 4, 5],
    [6, 7, 8, 9],
    [10, 11, 12, 13],
    [14, 15, 16, 17]
]
k = 960
print(solve(T,k))


