def podciag(T):
    N = len(T)
    maxi = 0

    for i in range(N - 1):
        suma_el = T[i]
        suma_ind = i
        cnt = 0
        for j in range(i + 1, N):
            if T[j - 1] < T[j]:
                suma_el += T[j]
                suma_ind += j
                cnt += 1
            else:    
                if suma_el == suma_ind:
                    maxi = max(maxi, cnt)
                break
        #end while
    #end while
            
    return maxi + 1 if maxi > 0 else 0

print(podciag([0,1,2,3,4,5,5,5,5,7,7,7,]))
