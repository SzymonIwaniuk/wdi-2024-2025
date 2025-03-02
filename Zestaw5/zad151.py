#Zadanie 151. W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy
#króla nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra
#liczby na polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do
#obranego celu (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest
#globalna tablica T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik
#ma współrzędne w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do
#prawego dolnego narożnika.
from math import log10

def first(num):
    l = int(log10(num)) + 1

    return num // 10**(l - 1)

def last(num):

    return num % 10


def king(T):
    memo = [[False for _ in range(8)] for _ in range(8)]
    moves = [(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)]
    def rek(r,c,T,memo,moves):
        if r == 7 and c == 7:
            return True
        if memo[r][c]:
            return False

        memo[r][c] = True

        for x,y in moves:
            if 8 > r + x >= 0 and 8 > c + y >= 0 and last(T[r][c]) < first(T[r + x][c + y]):
                if rek(r + x, c + y,T,memo,moves):
                    return True

        memo[r][c] = False
        return False

    return rek(0,0,T,memo,moves)

T = [
    [79, 14, 30, 32, 52, 70, 42, 70],
    [12, 14, 86, 52, 95, 90, 54, 30],
    [81, 63, 64, 92, 65, 97, 85, 95],
    [87, 90, 50, 91, 91, 92, 74, 32],
    [85, 76, 43, 76, 32, 72, 80, 75],
    [72, 30, 10, 41, 43, 40, 73, 71],
    [95, 43, 61, 83, 64, 96, 62, 94],
    [90, 71, 53, 20, 21, 70, 93, 74],
]

print(king(T))