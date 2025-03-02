def podciag(T):
    result = 0
    N = len(T)
    
    for i in range(N):
        cnt = 1
        q = None
        
        for j in range(i, N):
            if q is None:
                q = T[j] / T[j - 1]
                
            if T[j] / T[j - 1] == q: 
                
                cnt += 1
                
            else: break
            
        result = max(result, cnt)
        
        if result >= N - i: return result


T = [8, 1, 2, 1, 0.5, 0.25, 6, 7, 8, 10, 9, 10]

print(podciag(T))
