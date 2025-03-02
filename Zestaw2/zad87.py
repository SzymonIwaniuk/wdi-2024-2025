from math import sqrt


T = [1,3,3,4,9,12,25]

def isprime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is a prime number
    if n % 2 == 0:
        return False
    if n == 3:
        return True  # 3 is a prime number
    if n % 3 == 0:
        return False

    limit = int(sqrt(n)) + 1
    x = 5
    while x <= limit:
        if n % x == 0 or n % (x + 2) == 0:
            return False
        x += 2  # Increment by 2 first
        if x <= limit and n % x == 0:
            return False
        x += 4  # Then increment by 5

    return True

def zad87(T):
    N = len(T)
    result = 0
    
    for i in range(1, N):
        n = T[i]
        iloraz = 1
        j = 0

        while j < i:
            if isprime(T[j]):
                        iloraz *= T[j]
            j += 1
                        
        if n == T[j] and iloraz > result:
            result = iloraz

    if result != 0: return result
    else: return None

print(zad87(T)) 
