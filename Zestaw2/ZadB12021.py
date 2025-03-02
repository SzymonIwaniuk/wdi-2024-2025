def system4(n):
    liczba = 0
    place_value = 1
    
    while n > 0: 
        liczba += (n % 4) * place_value
        n //= 4
        place_value *= 10
        
    return liczba

def identyczne(a, b):

    T = [0 for _ in range(10)]

    while a > 0:
        if T[a % 10] < 1:
            T[a % 10] += 1

        a //= 10

    while b > 0:
        if T[b % 10] > 0:
            b //= 10
            
        else: return False


    return True



def podciag(T):
    N = len(T)
    maxi = 0

    for i in range(N):
        cnt = 1
        for j in range(i + 1, N):
            if identyczne(system4(T[i]), system4(T[j])):
                cnt += 1
                
            else: break

        maxi = max(cnt, maxi)
        if maxi >= N - i:  return maxi 
    

print(podciag([13, 23, 18, 33, 107, 57, 13, 509]))
            
 

