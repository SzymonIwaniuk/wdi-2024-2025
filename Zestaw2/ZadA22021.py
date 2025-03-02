from math import sqrt 


def is_prime(n):
    if n <= 1: return False
    elif n == 2 or n == 3: return True
    elif n % 2 == 0 or n % 3 == 0: return False

    i = 5

    while i <= sqrt(n):
        if n % i == 0: return False

        i += 2

        if n % i == 0: return False

        i += 4

    return True



def main(T):
    N = len(T)
    result = 0
    wynik = None
    
    for i in range(1, N):
        tmp = 1
        
        for j in range(i):
            if is_prime(T[j]):
                tmp *= T[j]

        if tmp == T[i] and T[i] > result and not is_prime(T[i]):
            wynik = i 

    return wynik
    
print(main([2,4,2,6,3,5,73, 2 ,73]))             
                
                
                
                    
                
            



    
