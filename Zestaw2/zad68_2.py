def solve(T):
    N = len(T)
    dl = dl_max = 1
    
    for i in range(N - 1):
        if T[i] < T[i + 1]: dl += 1

        else: 
            dl = 1

        dl_max = max(dl, dl_max)

    return dl_max


print(solve([1,2,3,4,2,7,5,1,2,3,4,5,6]))
