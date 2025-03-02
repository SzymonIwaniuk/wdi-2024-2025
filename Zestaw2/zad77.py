def czy_palindrom(T, i, j):
    while i <= j:
        if T[i] % 2 == 0: return False
        if T[i] != T[j]: return False
        i += 1
        j -= 1

    return True
    



def naj(T):
    dl = 0
    N = len(T)
    
    for i in range(N):
        if T[i] % 2 == 1:
            for j in range(i + 1, N):
                if czy_palindrom(T,i,j):
                    dl = max(dl, j - i + 1)
    return dl

print(naj([1,3,1,3,1,2,3,4,1,2,1]))
