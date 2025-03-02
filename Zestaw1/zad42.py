from math import log10



def zad42(a, b):
    while a:
        temp_a = a
        temp1 = a % 10
        temp_b = b
        cnt_a = 0
        cnt_b = 0
        

        while temp_a:
            if temp1 == temp_a % 10: cnt_a += 1

            temp_a //= 10

        while temp_b:
            if temp_b % 10 == temp1: cnt_b += 1

            temp_b //= 10

        if cnt_a != cnt_b: return False

        a //= 10

    return True

print(zad42(5749, 4597))
            
            
    
