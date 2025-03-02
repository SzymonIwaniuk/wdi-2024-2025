from math import ceil

def czy_wielokrotny(T, l_napis, n, napis):
    cnt = 0
    start = 0
    while start + l_napis < n:
        start += l_napis
        if T[start:start + l_napis] == napis:
            cnt += 1
        else:
            break
    return cnt

def multi(T):
    n = len(T)
    result = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            napis = T[i:j]
            l_napis = len(napis)
            cnt = czy_wielokrotny(T[i:], l_napis, n - i, napis) 
            result = max(result, cnt)

    return result

print(multi('ABCABCABCAAAAABAABA'))
