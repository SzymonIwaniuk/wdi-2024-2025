def silnia(n):
    result = 1
    if n==0:
        return 1
    for i in range(1,n+1):
        result *= i

    return result

def euler():
    N = 1000
    e = 0
    
    for j in range(0, N + 1):
        e += 1 / silnia(j)

    return e 
        
print(euler())
