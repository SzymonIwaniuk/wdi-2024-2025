def zad9():
    a = 1
    b = 1
    product = int( input() ) 

    while a * b <= product:
        if product == a * b: return True, a, b
        a, b = b, a + b
    return False 

print( zad9() )
