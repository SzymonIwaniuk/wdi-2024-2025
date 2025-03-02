def solve(T):
    N = len(T)
    dl = dl_max = 2
    
    for i in range(1, N - 1):
        q = T[i] / T[i - 1] if T[i - 1] != 0 else None

        if q is None: continue
        else:
            if T[i] * q == T[i + 1]: dl += 1

            else:  dl = 2

        dl_max = max(dl, dl_max)

    return dl_max


print(solve([1,2,3,4,2,7,5,6,3,1.5,0.75,2,1]))
