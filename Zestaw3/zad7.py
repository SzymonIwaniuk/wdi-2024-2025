from random import randint


def is_odd_number(n):
    while n > 0:
        if (n % 10) % 2 != 1: return False
        else: n //= 10

    return True

def list_check(tab, n):
    for el in tab:
        if is_odd_number(el): return "Zawiera", tab
        else: pass

    #end for
    return "Nie zawiera", tab
        
        
            


n = int( input() )
tab = [randint(1 , 1000) for _ in range(0, n)]
print( list_check(tab, n) )

