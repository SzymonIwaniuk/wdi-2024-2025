#Zadanie 107. Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję która
#odpowiada na pytanie, czy w tablicy każdy wiersz zawiera co najmniej jedną liczbą złożoną wyłącznie z cyfr
#będących liczbami pierwszymi?

def solve(T):
    N = len(T)

    for i in range(N):
        for j in range(N):
            f3 = True
            num = T[i][j]
            while num > 0:
                if not(num % 2 == 1 and 2 <= num % 10 <= 7):
                    f3 = False
                num //= 10
            if f3: return True


    return False

T = [
    [6676,4442,4544],
    [357,444,444],
    [4444,68,66]
                 ]
print(solve(T))