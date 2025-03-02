
        



def zad1():
    n = 13 * 8
    a = 0
    b = 1 # a , b fibbonaci jeden

    while a <= n:
        a , b = b , a + b
        c = int(n / a)
        d = 0
        e = 1 # d , e fibbonaci dwa 
    
        
        while d <= c:
            d , e = e , d + e 
            if d * a == n: # sprawdzanie warunku czy liczba jest iloczynem fib1 i fib2
                return True

    return False

print(zad1())
