def is_seq(n):
    a = 1
    b = 2

    while n >= a:
        a, b = b, a + b - 1
        
        if b == n: return True

    return False 

def seq(T):
    N = len(T)
    result = 0
    
    for i in range(N):
        for j in range(N):
            if is_seq(T[i][j]):
                tmp_i = i
                tmp_j = j
                cnt1 = 0
                cnt2 = 0
                
                while tmp_i < N and is_seq(T[tmp_i][j]):
                    cnt1 += 1
                    tmp_i += 1

                while tmp_j < N and is_seq(T[i][tmp_j]):
                    cnt2 += 1
                    tmp_j += 1

                result = max(result, cnt1, cnt2)
        
    return result

T = [[8, 2, 2, 3], [5, 2, 3, 10], [2, 3, 4, 0], [1, 4, 5, 5]]

print(seq(T))
