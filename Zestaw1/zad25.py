from math import sqrt

def is_fib(n):
    a = 1
    b = 1

    while b <= n:
        if n == b:
            return True
        a, b = b, a + b

    return False 



def zad25(x):
    a = 1
    b = 1

    while b <= sqrt(x):
        if x % b == 0:
            if is_fib(x // b):
                return True

        a, b = b, a + b

    return False
                

print( zad25(26) )
