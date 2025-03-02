#Zadanie 135. Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi
#zawierającymi koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i
#kolumnie k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy
#minimalny koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt
#przebywania na polu startowym i ostatnim także wliczamy do kosztu przejścia


def king(T, k):

    moves = [(1,-1),(1, 0),(1, 1)]
    cnt = T[0][k]

    def rek(cnt,w,k,T,moves):
        if w == 7:
            return cnt

        mini = 1e10

        for x,y in moves:
            wprim, kprim = w + x, k + y
            if 0 <= kprim < 8:
                result = rek(cnt + T[wprim][kprim], wprim, kprim, T, moves)
                mini = min(mini, result)

        return mini

    result = rek(cnt,0,k,T,moves)
    return result

T = [[17, 1, 18, 2, 10, 6, 18, 17],
    [19, 18, 6, 17, 7, 18, 8, 2],
    [3, 19, 13, 1, 15, 7, 8, 4],
    [19, 5, 17, 2, 16, 20, 15, 19],
    [16, 13, 18, 8, 7, 15, 8, 8],
    [15, 19, 15, 20, 7, 13, 6, 13],
    [14, 17, 11, 16, 7, 13, 14, 12],
    [15, 7, 8, 18, 4, 13, 15, 18]]

print(king(T,1))