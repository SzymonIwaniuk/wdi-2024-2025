def sito(n):
    tab = [0 for _ in range(n + 1)]
    tab[0] = tab[1] = 1
    i = 2

    while i*i <= n:
        if tab[i] == 0:
            for j in range(i*i, n + 1, i):
                tab[j] = 1
        i += 1

    return tab

# --- main
n = int( input() )

tab = sito(n)

for i in range(n + 1):
    if tab[i] == 0:
        print(i, end =' ')
