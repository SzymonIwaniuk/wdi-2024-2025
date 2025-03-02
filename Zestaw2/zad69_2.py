def solve(T):
    N = len(T)
    dl = dl_max = 2
    
    for i in range(1, N - 1):
        r = T[i] - T[i - 1]
        if T[i] + r == T[i + 1]: dl += 1

        else: 
            dl = 2

        dl_max = max(dl, dl_max)

    return dl_max


print(solve([1,2,3,4,2,7,5,6,5,4,3,2,1]))
