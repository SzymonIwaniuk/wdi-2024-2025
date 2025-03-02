def zad13():
    n = 3445531
    temp_n = n // 10
    
    while temp_n > 1:
        if temp_n % 10 == n % 10:
            return False
        temp_n //= 10
    return True 























print(zad13())    
