T = [13, 23, 18, 102, 33, 107, 57]

def same_digits(a, b):
    T = [0 for _ in range(10)]
    
    while a > 0:
        if T[a % 10] == 0: 
            T[a % 10] += 1
        a //= 10

    #end while
        
    while b > 0:
        if T[b % 10] != 0: 
            T[b % 10] -= 1

        if T[b % 10] < 0: return False
        
        b //= 10

    return sum(T) == 0 
    



def zamien_sys(x):
    result = 0

    while x > 0:
        result = result * 10 + x % 4
        x //= 4

    return result

def podciag(T):
    N = len(T)
    result = 0
    
    for i in range(1, N):
        n1 = zamien_sys(T[i])
        cnt = 0
        
        for j in range(i):
            n2 = zamien_sys(T[j])
            
            if same_digits(n1, n2):
                if cnt == 0:
                    cnt += 2
                else:
                    cnt += 1
        #end for
        
        if cnt > result:
            result = cnt
    # end for
    
    return result 
        
print(podciag(T))
