from math import log10

def zad43(N, s):
    eps = 1e-10
    a = 10 ** (N - 1)
    b = 10 ** N
    result = 0
    
    for i in range(a, b):
        suma = 0
        temp = i

        while temp:
            suma += (temp % 10) ** N
            temp //= 10

        if suma == s and i >= result:
            result = i
        
    return result

print(zad43(2, 162))
    
            
    
