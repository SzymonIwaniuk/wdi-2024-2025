#Zadanie 93. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
#odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
#z nieparzystych cyfr

def solve(T):
    N = len(T)
    f1 = True #Zakładamy ze w kazdym wierszu jest liczba nieparzysta zlozona z cyfr niparzystych
    for w in range(N):
        f2 = False #Co najmniej jedna; Zakładamy że nie istnieje co najmniej jedna

        for k in range(N):
            f3 = True #Dla każdego zakładamy, że jest nieparzytsa
            num = T[w][k]
            while num > 0:

                if num % 2 == 0:
                    f3 = False
                num //= 10
            if f3 : f2 = True
        #end for
        if not f2: f1 = False
    #end for
    return f1 

T = [[23, 85, 34, 55, 12],
 [98, 41, 77, 18, 69],
 [43, 64, 11, 92, 37],
 [49, 88, 61, 15, 25],
 [79, 10, 94, 32, 56]]

print(solve(T))
