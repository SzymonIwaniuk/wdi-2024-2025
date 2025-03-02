#Zadanie 158. Tablica t[N] jest wypełniona liczbami naturalnymi. Skok z pola i-tego można wykonać
#na pola o indeksach i+k, gdzie k jest czynnikiem pierwszym liczby t[i] (mniejszym od niej samej). Napisz
#funkcję, która sprawdza, czy da się przejść z pola 0 do N-1 – jeśli się da, zwraca ilość skoków, jeśli się nie
#da, zwraca -1.
def primes(num):
    if num < 4:
        return
    tab = []
    i = 2
    while i*i <= num:
        if num % i == 0:
            tab += [i]

        while num % i == 0:
            num //= i

        i += 1
    return tab



def solve(t,i,visited,jumps):
    if i == len(t) - 1:
        return jumps
    if visited[i]:
        return 1e10

    visited[i] = True
    min_j = 1e10

    for x in primes(t[i]):
        if i + x < len(t):
            min_j = min(min_j, solve(t,i+x, visited,jumps + 1))

    visited[i] = False
    return min_j if min_j != 1e10 else -1

t = [10, 15, 6, 8, 3]
visited = [False] * len(t)
print(solve(t, 0,visited,0 ))