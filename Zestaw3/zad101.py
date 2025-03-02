#Zadanie 101. Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca war-
#tość True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz wartość
#False w przeciwnym przypadku.

#TODO: zredukuj flagi (kwantyfikatory)

def zeros(T):
    N = len(T)
    f1 = True
    for i in range(N):
        f2 = True
        for j in range(N):
            f3 = False
            if T[i][j] == 0:
                f3 = True
        if not f3: f2 = False
    if not f2: f1 = False
    return f1

T = [
    [1, 0, 3, 4, 5],
    [6, 7, 0, 9, 10],
    [11, 0, 13, 14, 15],
    [16, 17, 18, 0, 19],
    [20, 21, 22, 23, 0]
]
T_no_zeros = [
    [1, 2, 3, 4, 0],
    [6, 7, 8, 0, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 0, 23, 24, 25]
]



print(zeros(T_no_zeros))


