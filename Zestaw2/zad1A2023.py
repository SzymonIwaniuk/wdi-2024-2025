T = [2, 3, 4, 5, 7, 6, 23, 24, 12, 13, 14, 15, 16, 45, 15]


def parami_zgodne(n1, n2):
    if n1 >= n2:
        higher = n1
        lower = n2
    else:
        higher = n2
        lower = n1

    i = 2

    while i <= lower:
        if lower % i == 0 and higher % i == 0:
            while higher % i == 0:
                higher //= i

            while lower % i == 0:
                lower //= i

        i += 1

    if higher == 1 and lower == 1:
        return True
    else:
        return False 





def zgodne(T):
    N = len(T)
    counter = 0
    for i in range(N):
        
        for j in range(N):
            
            if abs(i - j) < 3:

                if parami_zgodne(T[i], T[j]):
                    counter += 1
                    
                #end if
            #end if
        #end for
    #end for
    return counter // 3

print(zgodne(T))
                
