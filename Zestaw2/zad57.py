from math import sqrt, log10

def sys(s, n):
    pom = 1
    bud = 0
    
    while n != 0:
        bud += (n % s) * pom
        n //= s
        pom *= 10

    return bud

def is_prime(n):
    if n <= 1: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False

    i = 5

    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 2

        if n % i == 0:
            return False
        i += 4

    return True

def rotacja(n, l):
    last_digit = n % 10
    remainder = n // 10
    return last_digit * (10 ** (l - 1)) + remainder

def iloczyn(n):
    iloczyn = 1
    while n:
        iloczyn *= (n % 10)
        n //= 10
    return iloczyn

############################################################################################
############################################################################################

def ilo_pierw(n):
    mini = 17 
    l = int(log10(n)) + 1

    for r in range(l):
        n = rotacja(n, l)
        
        
        for s in range(3, 17):
            tmp = sys(s, n)
            
            if is_prime(iloczyn(tmp)):
                
                mini = min(s, mini)
                
                
            

    if mini == 17: return None
    else: return mini

print(ilo_pierw(16))

            
